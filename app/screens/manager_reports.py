from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
<ManagerReportsScreen>:
    name: "manager_reports"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(12)
        spacing: dp(8)
        MDTopAppBar:
            title: "Reports & Analytics"
            left_action_items: [["arrow-left", lambda x: app.go("manager_dashboard")]]
            right_action_items: [["home-outline", lambda x: app.go("manager_dashboard")]]
        MDLabel:
            id: analytics
            text: "Analytics"
'''
Builder.load_string(KV)


class ManagerReportsScreen(BaseScreen):
    def on_pre_enter(self, *args):
        data = self.app.load_manager_analytics()
        self.ids.analytics.text = (
            f"Avg Progress: {data.get('avg_progress', 0)}%\n"
            f"Completed: {data.get('completed_courses', 0)}\n"
            f"Overdue: {data.get('overdue_courses', 0)}\n"
            f"Top-5: {', '.join(data.get('top5', [])) if data.get('top5') else '-'}"
        )
