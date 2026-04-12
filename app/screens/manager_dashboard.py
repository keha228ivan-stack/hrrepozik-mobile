from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
<ManagerDashboardScreen>:
    name: "manager_dashboard"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Manager Dashboard"
            right_action_items: [["account", lambda x: app.go("profile")]]
        MDBoxLayout:
            orientation: "vertical"
            padding: dp(12)
            MDLabel:
                id: summary
                text: "Team KPIs"
            MDRaisedButton:
                text: "Employees"
                on_release: app.go("employees")
'''
Builder.load_string(KV)


class ManagerDashboardScreen(BaseScreen):
    def on_pre_enter(self, *args):
        team = self.app.load_employees()
        avg = int(sum([e.avg_progress for e in team]) / len(team)) if team else 0
        self.ids.summary.text = f"Employees: {len(team)} | Average Progress: {avg}%"
