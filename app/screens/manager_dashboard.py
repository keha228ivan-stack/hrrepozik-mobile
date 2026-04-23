from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
#:import get_color_from_hex kivy.utils.get_color_from_hex
<ManagerDashboardScreen>:
    name: "manager_dashboard"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")

        MDBoxLayout:
            size_hint_y: None
            height: dp(112)
            padding: dp(24), dp(20), dp(24), dp(16)
            spacing: dp(16)
            md_bg_color: [1, 1, 1, 1]

            MDBoxLayout:
                orientation: "vertical"

                MDLabel:
                    text: "Система управления персоналом"
                    font_style: "H5"
                    bold: True
                    theme_text_color: "Primary"

                MDLabel:
                    text: "Учёт персонала, обучения и оценки эффективности"
                    theme_text_color: "Secondary"

            Widget:

            MDIconButton:
                icon: "bell-outline"
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex("#64748B")
                on_release: app.go("notifications")

            MDIconButton:
                icon: "cog-outline"
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex("#64748B")
                on_release: app.go("settings")

            MDIconButton:
                icon: "logout"
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex("#64748B")
                on_release: app.logout()

            MDRectangleFlatButton:
                text: "💼 Менеджер"
                size_hint: None, None
                size: dp(160), dp(52)
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
                    text_color: get_color_from_hex("#64748B")
                    icon_color: get_color_from_hex("#64748B")

                MDRectangleFlatIconButton:
                    text: "Сотрудники"
                    icon: "account-group-outline"
                    line_color: [0, 0, 0, 0]
                    text_color: get_color_from_hex("#64748B")
                    icon_color: get_color_from_hex("#64748B")
                    on_release: app.go("employees")

                MDRectangleFlatIconButton:
                    text: "Обучение"
                    icon: "book-open-page-variant-outline"
                    line_color: [0, 0, 0, 0]
                    text_color: get_color_from_hex("#64748B")
                    icon_color: get_color_from_hex("#64748B")
                    on_release: app.go("course_list")

                MDRectangleFlatIconButton:
                    text: "Оценка"
                    icon: "chart-line"
                    line_color: [0, 0, 0, 0]
                    text_color: get_color_from_hex("#64748B")
                    icon_color: get_color_from_hex("#64748B")
                    on_release: app.go("manager_reports")

                MDRaisedButton:
                    text: "Создать курс"
                    icon: "clipboard-plus-outline"
                    size_hint_y: None
                    height: dp(48)
                    md_bg_color: get_color_from_hex("#2563EB")

                MDRectangleFlatIconButton:
                    text: "Библиотека"
                    icon: "bookshelf"
                    line_color: [0, 0, 0, 0]
                    text_color: get_color_from_hex("#64748B")
                    icon_color: get_color_from_hex("#64748B")

                MDRectangleFlatIconButton:
                    text: "Отчёты"
                    icon: "file-chart-outline"
                    line_color: [0, 0, 0, 0]
                    text_color: get_color_from_hex("#64748B")
                    icon_color: get_color_from_hex("#64748B")
                    on_release: app.go("manager_reports")

                Widget:

            ScrollView:
                do_scroll_x: False

                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: dp(28), dp(24), dp(28), dp(28)
                    spacing: dp(16)

                    MDLabel:
                        text: "Создание курса"
                        font_style: "H5"
                        bold: True
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Настройка новой программы обучения"
                        theme_text_color: "Secondary"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        id: summary
                        text: ""
                        theme_text_color: "Secondary"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDCard:
                        orientation: "vertical"
                        padding: dp(20)
                        spacing: dp(16)
                        radius: [18, 18, 18, 18]
                        elevation: 0
                        md_bg_color: [1, 1, 1, 1]
                        size_hint_y: None
                        height: dp(560)

                        MDLabel:
                            text: "Основная информация"
                            font_style: "H6"
                            bold: True

                        MDGridLayout:
                            cols: 2
                            spacing: dp(16)
                            adaptive_height: True

                            MDTextField:
                                hint_text: "Название курса"
                                helper_text: "Введите название курса"
                                helper_text_mode: "persistent"
                                mode: "rectangle"

                            MDTextField:
                                hint_text: "Категория"
                                text: "Разработка"
                                mode: "rectangle"

                            MDTextField:
                                hint_text: "Длительность"
                                helper_text: "Например: 4 недели"
                                helper_text_mode: "persistent"
                                mode: "rectangle"

                            MDTextField:
                                hint_text: "Уровень сложности"
                                text: "Начальный"
                                mode: "rectangle"

                        MDTextField:
                            hint_text: "Дедлайн прохождения"
                            text: "дд.мм.гггг"
                            mode: "rectangle"

                        MDTextField:
                            hint_text: "Описание курса"
                            helper_text: "Опишите содержание и цели курса"
                            helper_text_mode: "persistent"
                            mode: "rectangle"
                            multiline: True
                            max_height: dp(180)
'''
Builder.load_string(KV)


class ManagerDashboardScreen(BaseScreen):
    def on_pre_enter(self, *args):
        team = self.app.load_employees()
        avg = int(sum([e.avg_progress for e in team]) / len(team)) if team else 0
        analytics = self.app.load_manager_analytics()
        self.ids.summary.text = (
            f"Сотрудников: {len(team)} • Средний прогресс: {avg}% • "
            f"Завершено курсов: {analytics.get('completed_courses', 0)} • "
            f"Просрочено: {analytics.get('overdue_courses', 0)}"
        )
