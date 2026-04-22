from kivy.lang import Builder
from kivymd.toast import toast

from app.screens.base import BaseScreen
from app.services.api_client import APIError

KV = '''
#:import dp kivy.metrics.dp
#:import get_color_from_hex kivy.utils.get_color_from_hex
<LoginScreen>:
    name: "login"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")

        MDTopAppBar:
            title: "Вход"

        AnchorLayout:
            anchor_x: "center"
            anchor_y: "center"

            MDCard:
                orientation: "vertical"
                size_hint: None, None
                size: dp(420), dp(430)
                padding: dp(24)
                spacing: dp(12)
                radius: [18, 18, 18, 18]
                elevation: 0
                md_bg_color: [1, 1, 1, 1]

                MDLabel:
                    text: "Вход в систему"
                    halign: "center"
                    font_style: "H5"
                    bold: True

                MDLabel:
                    text: "Используй email и пароль"
                    halign: "center"
                    theme_text_color: "Secondary"

                MDTextField:
                    id: email
                    hint_text: "Email"
                    mode: "rectangle"

                MDTextField:
                    id: password
                    hint_text: "Пароль"
                    mode: "rectangle"
                    password: True

                MDRaisedButton:
                    text: "Войти"
                    on_release: root.on_login()

                MDTextButton:
                    text: "Нет аккаунта? Регистрация"
                    pos_hint: {"center_x": .5}
                    on_release: app.go("register")
'''
Builder.load_string(KV)


class LoginScreen(BaseScreen):
    _submitting = False

    def on_login(self) -> None:
        if self._submitting:
            return
        self._submitting = True
        email = self.ids.email.text.strip()
        password = self.ids.password.text
        if not email or not password:
            toast("Введи email и пароль")
            self._submitting = False
            return
        try:
            self.app.handle_login(email, password)
            toast("Вход выполнен")
        except APIError as exc:
            toast(f"Ошибка входа: {exc}")
        finally:
            self._submitting = False
