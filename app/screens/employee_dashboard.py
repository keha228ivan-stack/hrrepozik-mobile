from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
#:import get_color_from_hex kivy.utils.get_color_from_hex
<EmployeeDashboardScreen>:
    name: "employee_dashboard"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")

        MDBoxLayout:
            size_hint_y: None
            height: dp(106)
            padding: dp(24), dp(20), dp(24), dp(16)
            spacing: dp(16)
            md_bg_color: [1, 1, 1, 1]

            MDBoxLayout:
                orientation: "vertical"
                spacing: dp(4)

                MDLabel:
                    text: "Система управления персоналом"
                    font_style: "H5"
                    bold: True
                    theme_text_color: "Primary"

                MDLabel:
                    text: "Мой прогресс и активные курсы"
                    theme_text_color: "Secondary"

            Widget:

            MDIconButton:
                icon: "bell-outline"
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex("#64748B")
                on_release: app.go("notifications")

            MDIconButton:
                icon: "account-outline"
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex("#64748B")
                on_release: app.go("profile")

            MDIconButton:
                icon: "logout"
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex("#64748B")
                on_release: app.logout()

            MDRectangleFlatButton:
                text: "👤 Сотрудник"
                size_hint: None, None
                size: dp(170), dp(46)
                line_color: get_color_from_hex("#CBD5E1")
                text_color: get_color_from_hex("#0F172A")
                on_release: app.go("profile")

        MDBoxLayout:
            MDBoxLayout:
                orientation: "vertical"
                size_hint_x: None
                width: dp(250)
                padding: dp(16), dp(16)
                spacing: dp(12)
                md_bg_color: [1, 1, 1, 1]

                MDRectangleFlatIconButton:
                    text: "Dashboard"
                    icon: "view-dashboard-outline"
                    line_color: [0, 0, 0, 0]
                    text_color: get_color_from_hex("#2563EB")
                    icon_color: get_color_from_hex("#2563EB")

                MDRectangleFlatIconButton:
                    text: "Курсы"
                    icon: "book-open-page-variant-outline"
                    line_color: [0, 0, 0, 0]
                    text_color: get_color_from_hex("#64748B")
                    icon_color: get_color_from_hex("#64748B")
                    on_release: app.go("course_list")

                MDRectangleFlatIconButton:
                    text: "Результаты"
                    icon: "chart-line"
                    line_color: [0, 0, 0, 0]
                    text_color: get_color_from_hex("#64748B")
                    icon_color: get_color_from_hex("#64748B")
                    on_release: app.go("progress_results")

                MDRectangleFlatIconButton:
                    text: "Микрозадачи"
                    icon: "check-decagram-outline"
                    line_color: [0, 0, 0, 0]
                    text_color: get_color_from_hex("#64748B")
                    icon_color: get_color_from_hex("#64748B")
                    on_release: app.go("microtasks")

                MDRectangleFlatIconButton:
                    text: "Достижения"
                    icon: "trophy-outline"
                    line_color: [0, 0, 0, 0]
                    text_color: get_color_from_hex("#64748B")
                    icon_color: get_color_from_hex("#64748B")
                    on_release: app.go("achievements")

                Widget:

            ScrollView:
                do_scroll_x: False
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: dp(28), dp(24), dp(28), dp(28)
                    spacing: dp(16)

                    MDLabel:
                        text: "Dashboard"
                        font_style: "H5"
                        bold: True
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Обзор ключевых метрик обучения"
                        theme_text_color: "Secondary"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDGridLayout:
                        cols: 3
                        spacing: dp(14)
                        adaptive_height: True
                        size_hint_y: None
                        height: dp(140)

                        MDCard:
                            orientation: "vertical"
                            padding: dp(18)
                            radius: [16, 16, 16, 16]
                            elevation: 0
                            md_bg_color: [1, 1, 1, 1]
                            MDLabel:
                                text: "Всего курсов"
                                theme_text_color: "Secondary"
                            MDLabel:
                                id: courses_total
                                text: "0"
                                font_style: "H4"
                                bold: True

                        MDCard:
                            orientation: "vertical"
                            padding: dp(18)
                            radius: [16, 16, 16, 16]
                            elevation: 0
                            md_bg_color: [1, 1, 1, 1]
                            MDLabel:
                                text: "Активные"
                                theme_text_color: "Secondary"
                            MDLabel:
                                id: courses_active
                                text: "0"
                                font_style: "H4"
                                bold: True

                        MDCard:
                            orientation: "vertical"
                            padding: dp(18)
                            radius: [16, 16, 16, 16]
                            elevation: 0
                            md_bg_color: [1, 1, 1, 1]
                            MDLabel:
                                text: "Завершено"
                                theme_text_color: "Secondary"
                            MDLabel:
                                id: courses_completed
                                text: "0"
                                font_style: "H4"
                                bold: True

                    MDCard:
                        orientation: "vertical"
                        padding: dp(20)
                        spacing: dp(10)
                        radius: [16, 16, 16, 16]
                        elevation: 0
                        md_bg_color: [1, 1, 1, 1]
                        size_hint_y: None
                        adaptive_height: True

                        MDLabel:
                            text: "Сводка"
                            font_style: "H6"
                            bold: True

                        MDLabel:
                            id: summary
                            text: "Loading..."
                            theme_text_color: "Secondary"
                            adaptive_height: True

                    MDCard:
                        orientation: "vertical"
                        padding: dp(16)
                        radius: [16, 16, 16, 16]
                        elevation: 0
                        md_bg_color: [1, 1, 1, 1]
                        adaptive_height: True

                        MDLabel:
                            text: "Мои курсы"
                            font_style: "H6"
                            bold: True
                            adaptive_height: True

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
        self.ids.courses_total.text = str(len(self.app.state.courses))
        self.ids.courses_active.text = str(active)
        self.ids.courses_completed.text = str(completed)
        self.ids.summary.text = (
            f"Courses: {len(self.app.state.courses)} | Active: {active} | Completed: {completed} | "
            f"Overdue: {overdue} | Notifications: {len(self.app.state.notifications)}"
        )
