from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
<EmployeeDashboardScreen>:
    name: "employee_dashboard"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Employee Dashboard"
            right_action_items: [["account", lambda x: app.go("profile")]]
        ScrollView:
            MDList:
                id: course_list
'''
Builder.load_string(KV)


class EmployeeDashboardScreen(BaseScreen):
    def on_pre_enter(self, *args):
        self.app.load_courses()
        container = self.ids.course_list
        container.clear_widgets()
        for course in self.app.state.courses:
            container.add_widget(self.app.widgets.course_item(course, "course_detail"))
