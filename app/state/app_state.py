from dataclasses import dataclass, field
from typing import Callable

from app.models.course import Course
from app.models.notification import AppNotification
from app.models.user import User


@dataclass
class AppState:
    token: str | None = None
    user: User | None = None
    courses: list[Course] = field(default_factory=list)
    notifications: list[AppNotification] = field(default_factory=list)
    test_results: list[dict] = field(default_factory=list)
    assignment_results: list[dict] = field(default_factory=list)
    achievements: dict = field(default_factory=dict)
    loading: bool = False
    _subscribers: list[Callable[[], None]] = field(default_factory=list)

    def set_user(self, user: User | None) -> None:
        self.user = user
        self.emit()

    def set_token(self, token: str | None) -> None:
        self.token = token
        self.emit()

    def set_courses(self, courses: list[Course]) -> None:
        self.courses = courses
        self.emit()

    def set_notifications(self, notifications: list[AppNotification]) -> None:
        self.notifications = notifications
        self.emit()

    def set_learning(self, *, tests: list[dict], assignments: list[dict], achievements: dict) -> None:
        self.test_results = tests
        self.assignment_results = assignments
        self.achievements = achievements
        self.emit()

    def subscribe(self, callback: Callable[[], None]) -> None:
        self._subscribers.append(callback)

    def emit(self) -> None:
        for callback in self._subscribers:
            callback()
