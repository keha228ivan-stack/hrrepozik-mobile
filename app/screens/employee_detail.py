from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
<EmployeeDetailScreen>:
    name: "employee_detail"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(12)
        MDLabel:
            id: title
            text: "Employee"
        MDLabel:
            id: body
            text: "Details"
'''
Builder.load_string(KV)


class EmployeeDetailScreen(BaseScreen):
    def on_pre_enter(self, *args):
        data = self.app.selected_employee
        if not data:
            return
        self.ids.title.text = data.get("name", "Employee")
        self.ids.body.text = f"Progress: {data.get('avg_progress', 0)}% | KPI: {data.get('kpi', '-') }"
