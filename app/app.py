from __future__ import annotations

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from app.models.course import Course
from app.models.user import User
from app.services.api_client import APIClient, APIError, UnauthorizedError
from app.services.auth_service import AuthService
from app.services.course_service import CourseService
from app.services.employee_service import EmployeeService
from app.services.notification_service import NotificationService
from app.services.push_service import PushService
from app.services.sync_service import SyncService
from app.screens.login import LoginScreen
from app.screens.register import RegisterScreen
from app.screens.profile import ProfileScreen
from app.screens.employee_dashboard import EmployeeDashboardScreen
from app.screens.manager_dashboard import ManagerDashboardScreen
from app.screens.course_list import CourseListScreen
from app.screens.course_detail import CourseDetailScreen
from app.screens.employee_list import EmployeeListScreen
from app.screens.employee_detail import EmployeeDetailScreen
from app.screens.notifications import NotificationsScreen
from app.screens.settings import SettingsScreen
from app.state.app_state import AppState
from app.storage.cache_store import CacheStore
from app.storage.secure_store import SecureTokenStore
from app.widgets.course_widgets import CourseListItem


class WidgetFactory:
    def __init__(self, app: "HRLMSApp") -> None:
        self.app = app

    def course_item(self, course: Course, destination: str):
        return CourseListItem(course, on_open=lambda cid: self.app.open_course(cid, destination))


class HRLMSApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.state = AppState()
        self.api = APIClient()
        self.auth_service = AuthService(self.api)
        self.course_service = CourseService(self.api)
        self.employee_service = EmployeeService(self.api)
        self.notification_service = NotificationService(self.api)
        self.token_store = SecureTokenStore()
        self.cache_store = CacheStore()
        self.sync_service = SyncService(self.cache_store, self.course_service)
        self.push_service = PushService()
        self.widgets = WidgetFactory(self)
        self.selected_course_id: int | None = None
        self.selected_employee: dict | None = None

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        sm = ScreenManager()
        for screen in [
            LoginScreen(self),
            RegisterScreen(self),
            ProfileScreen(self),
            EmployeeDashboardScreen(self),
            ManagerDashboardScreen(self),
            CourseListScreen(self),
            CourseDetailScreen(self),
            EmployeeListScreen(self),
            EmployeeDetailScreen(self),
            NotificationsScreen(self),
            SettingsScreen(self),
        ]:
            sm.add_widget(screen)
        self.restore_session()
        return sm

    def go(self, screen_name: str):
        self.root.current = screen_name

    def handle_login(self, email: str, password: str):
        token = self.auth_service.login(email, password)
        self._establish_session(token)

    def handle_register(self, name: str, email: str, password: str):
        token = self.auth_service.register(name, email, password)
        self._establish_session(token)

    def _establish_session(self, token: str):
        self.api.set_token(token)
        self.token_store.save_token(token)
        self.state.set_token(token)
        user = self.auth_service.me()
        self.state.set_user(user)
        self.cache_store.set("profile", user.model_dump(mode="json"))
        self.push_service.initialize()
        self.route_by_role()

    def restore_session(self):
        token = self.token_store.get_token()
        if not token:
            self.go("login")
            return
        try:
            self._establish_session(token)
        except UnauthorizedError:
            self.logout()
        except APIError:
            self.state.set_token(token)
            self.api.set_token(token)
            cached = self.cache_store.get("profile")
            if cached:
                self.state.set_user(User.model_validate(cached))
            self.go("login")

    def logout(self):
        self.token_store.clear()
        self.state.set_token(None)
        self.state.set_user(None)
        self.api.set_token(None)
        self.go("login")

    def route_by_role(self):
        if not self.state.user:
            self.go("login")
        elif self.state.user.role == "manager":
            self.go("manager_dashboard")
        else:
            self.go("employee_dashboard")

    def load_courses(self):
        try:
            courses = self.course_service.list_courses({"page": 1, "page_size": 20})
            self.state.set_courses(courses)
            self.cache_store.set("courses", {"items": [c.model_dump(mode='json') for c in courses]})
        except APIError:
            cached = self.cache_store.get("courses")
            if cached:
                self.state.set_courses([Course.model_validate(item) for item in cached.get("items", [])])

    def open_course(self, course_id: int, destination: str = "course_detail"):
        self.selected_course_id = course_id
        self.go(destination)

    def get_selected_course(self) -> Course | None:
        for course in self.state.courses:
            if course.id == self.selected_course_id:
                return course
        return None

    def update_course_progress(self, course_id: int, progress: int):
        try:
            self.course_service.update_progress(course_id, progress)
        except APIError:
            self.sync_service.queue_progress(course_id, progress)

    def load_notifications(self):
        try:
            items = self.notification_service.list_notifications()
            self.state.set_notifications(items)
        except APIError:
            return

    def load_employees(self):
        try:
            return self.employee_service.list_employees({"page": 1, "page_size": 30})
        except APIError:
            return []

    def open_employee(self, user_id: int):
        self.selected_employee = self.employee_service.employee_detail(user_id)
        self.go("employee_detail")

    def flush_sync(self):
        self.sync_service.flush()
