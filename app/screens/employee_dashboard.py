from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
<EmployeeDashboardScreen>:
    name: "employee_dashboard"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Employee Dashboard"
            right_action_items: [["account", lambda x: app.go("profile")]]
        MDBoxLayout:
            adaptive_height: True
            spacing: dp(8)
            padding: dp(8)
            MDRaisedButton:
                text: "Courses"
                on_release: app.go("course_list")
            MDRaisedButton:
                text: "Results"
                on_release: app.go("progress_results")
            MDRaisedButton:
                text: "Microtasks"
                on_release: app.go("microtasks")
            MDRaisedButton:
                text: "Achievements"
                on_release: app.go("achievements")
        MDLabel:
            id: summary
            text: "Loading..."
            adaptive_height: True
        ScrollView:
            MDList:
                id: course_list
'''
Builder.load_string(KV)


class EmployeeDashboardScreen(BaseScreen):
    def on_pre_enter(self, *args):
        self.app.load_courses()
        self.app.load_notifications()
        container = self.ids.course_list
        container.clear_widgets()
        active = completed = overdue = 0
        for course in self.app.state.courses:
            if course.status == "active":
                active += 1
            elif course.status == "completed":
                completed += 1
            elif course.status == "overdue":
                overdue += 1
            container.add_widget(self.app.widgets.course_item(course, "course_detail"))
        self.ids.summary.text = (
            f"Courses: {len(self.app.state.courses)} | Active: {active} | Completed: {completed} | "
            f"Overdue: {overdue} | Notifications: {len(self.app.state.notifications)}"
        )
