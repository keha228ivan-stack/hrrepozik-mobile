from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
#:import get_color_from_hex kivy.utils.get_color_from_hex
<EmployeeDetailScreen>:
    name: "employee_detail"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")
        padding: dp(12)
        MDTopAppBar:
            title: "Детали сотрудника"
            left_action_items: [["arrow-left", lambda x: app.go("employees")]]
            right_action_items: [["home-outline", lambda x: app.go("manager_dashboard")]]
        MDLabel:
            id: title
            text: "Employee"
        MDLabel:
            id: body
            text: "Details"
        MDTextField:
            id: course_id
            hint_text: "Course ID for assignment"
        MDRaisedButton:
            text: "Assign course"
            on_release: root.assign_course()
'''
Builder.load_string(KV)


class EmployeeDetailScreen(BaseScreen):
    def on_pre_enter(self, *args):
        data = self.app.selected_employee
        if not data:
            return
        self.ids.title.text = data.get("name", "Employee")
        self.ids.body.text = f"Progress: {data.get('avg_progress', 0)}% | KPI: {data.get('kpi', '-') }"

    def assign_course(self):
        data = self.app.selected_employee
        if not data:
            return
        value = self.ids.course_id.text.strip()
        if not value.isdigit():
            return
        self.app.assign_course(int(data["user_id"]), int(value))
