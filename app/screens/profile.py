from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
#:import get_color_from_hex kivy.utils.get_color_from_hex
<ProfileScreen>:
    name: "profile"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")

        MDTopAppBar:
            title: "Профиль"
            left_action_items: [["arrow-left", lambda x: root.back_to_dashboard()]]
            right_action_items: [["home-outline", lambda x: root.back_to_dashboard()], ["logout", lambda x: app.logout()]]

        ScrollView:
            do_scroll_x: False
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(24)
                spacing: dp(16)

                MDCard:
                    orientation: "vertical"
                    radius: [18, 18, 18, 18]
                    elevation: 0
                    md_bg_color: [1, 1, 1, 1]
                    padding: dp(18)
                    spacing: dp(10)
                    adaptive_height: True

                    MDBoxLayout:
                        adaptive_height: True
                        spacing: dp(8)

                        MDLabel:
                            id: role_icon
                            text: "👤"
                            font_style: "H5"
                            size_hint_x: None
                            width: dp(36)

                        MDLabel:
                            id: role_header
                            text: "Меню сотрудника"
                            font_style: "H6"
                            bold: True

                    MDLabel:
                        id: name
                        text: "Имя:"
                    MDLabel:
                        id: email
                        text: "Email:"
                    MDLabel:
                        id: role
                        text: "Роль:"

                MDCard:
                    orientation: "vertical"
                    radius: [18, 18, 18, 18]
                    elevation: 0
                    md_bg_color: [1, 1, 1, 1]
                    padding: dp(18)
                    spacing: dp(12)
                    adaptive_height: True

                    MDLabel:
                        text: "Редактирование"
                        font_style: "H6"
                        bold: True

                    MDTextField:
                        id: name_input
                        hint_text: "Имя"
                        mode: "rectangle"

                    MDTextField:
                        id: department_input
                        hint_text: "Отдел"
                        mode: "rectangle"

                    MDRaisedButton:
                        text: "Сохранить профиль"
                        on_release: root.save_profile()

                    MDRectangleFlatButton:
                        text: "Выйти из аккаунта"
                        on_release: app.logout()
'''
Builder.load_string(KV)


class ProfileScreen(BaseScreen):
    def on_pre_enter(self, *args):
        user = self.app.state.user
        if not user:
            return
        role_ru = "Менеджер" if user.role == "manager" else "Сотрудник"
        self.ids.role_icon.text = "💼" if user.role == "manager" else "👤"
        self.ids.role_header.text = f"Меню: {role_ru}"
        self.ids.name.text = f"Имя: {user.name}"
        self.ids.name_input.text = user.name
        self.ids.email.text = f"Email: {user.email}"
        self.ids.role.text = f"Роль: {role_ru}"
        self.ids.department_input.text = user.department or ""

    def save_profile(self):
        self.app.update_profile(
            {"name": self.ids.name_input.text.strip(), "department": self.ids.department_input.text.strip()}
        )

    def back_to_dashboard(self):
        self.app.route_by_role()
