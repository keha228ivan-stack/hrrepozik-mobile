from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
<ManagerDashboardScreen>:
    name: "manager_dashboard"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: "#F4F7FB"
        MDTopAppBar:
            title: "Система управления персоналом"
            right_action_items: [["bell-outline", lambda x: app.go("notifications")], ["cog-outline", lambda x: app.go("settings")], ["account", lambda x: app.go("profile")]]
        MDBoxLayout:
            MDCard:
                orientation: "vertical"
                size_hint_x: .26
                radius: [0, 0, 0, 0]
                md_bg_color: "#FFFFFF"
                padding: dp(10)
                spacing: dp(4)
                MDList:
                    OneLineIconListItem:
                        text: "Dashboard"
                        on_release: app.go("manager_dashboard")
                        IconLeftWidget:
                            icon: "view-dashboard-outline"
                    OneLineIconListItem:
                        text: "Сотрудники"
                        on_release: app.go("employees")
                        IconLeftWidget:
                            icon: "account-group-outline"
                    OneLineIconListItem:
                        text: "Обучение"
                        on_release: app.go("course_list")
                        IconLeftWidget:
                            icon: "book-open-page-variant-outline"
                    OneLineIconListItem:
                        text: "Отчёты"
                        on_release: app.go("manager_reports")
                        IconLeftWidget:
                            icon: "file-chart-outline"
            ScrollView:
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: dp(16)
                    spacing: dp(12)
                    MDLabel:
                        text: "Dashboard"
                        font_style: "H5"
                        adaptive_height: True
                    MDLabel:
                        text: "Обзор ключевых метрик системы"
                        theme_text_color: "Secondary"
                        adaptive_height: True
                    MDGridLayout:
                        cols: 2
                        adaptive_height: True
                        spacing: dp(12)
                        MDCard:
                            padding: dp(14)
                            MDBoxLayout:
                                orientation: "vertical"
                                MDLabel:
                                    text: "Всего сотрудников"
                                MDLabel:
                                    id: total
                                    text: "0"
                                    font_style: "H4"
                        MDCard:
                            padding: dp(14)
                            MDBoxLayout:
                                orientation: "vertical"
                                MDLabel:
                                    text: "Активных"
                                MDLabel:
                                    id: active
                                    text: "0"
                                    font_style: "H4"
                        MDCard:
                            padding: dp(14)
                            MDBoxLayout:
                                orientation: "vertical"
                                MDLabel:
                                    text: "Средняя оценка"
                                MDLabel:
                                    id: avg
                                    text: "0%"
                                    font_style: "H4"
                        MDCard:
                            padding: dp(14)
                            MDBoxLayout:
                                orientation: "vertical"
                                MDLabel:
                                    text: "Пройдено курсов"
                                MDLabel:
                                    id: completed
                                    text: "0"
                                    font_style: "H4"
                    MDCard:
                        padding: dp(14)
                        MDLabel:
                            id: summary
                            text: "..."
'''
Builder.load_string(KV)


class ManagerDashboardScreen(BaseScreen):
    def on_pre_enter(self, *args):
        team = self.app.load_employees()
        analytics = self.app.load_manager_analytics()
        total = len(team)
        active = len([e for e in team if e.avg_progress > 0])
        self.ids.total.text = str(total)
        self.ids.active.text = str(active)
        self.ids.avg.text = f"{analytics.get('avg_progress', 0)}%"
        self.ids.completed.text = str(analytics.get("completed_courses", 0))
        self.ids.summary.text = (
            f"Overdue: {analytics.get('overdue_courses', 0)} | "
            f"Top-5: {', '.join(analytics.get('top5', [])) if analytics.get('top5') else '-'}"
        )
