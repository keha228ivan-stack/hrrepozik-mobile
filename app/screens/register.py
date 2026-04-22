from kivy.lang import Builder
from kivymd.toast import toast

from app.screens.base import BaseScreen
from app.services.api_client import APIError

KV = '''
#:import dp kivy.metrics.dp
#:import get_color_from_hex kivy.utils.get_color_from_hex
<RegisterScreen>:
    name: "register"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")

        MDTopAppBar:
            title: "Регистрация"
            left_action_items: [["arrow-left", lambda x: app.go("login")]]

        AnchorLayout:
            anchor_x: "center"
            anchor_y: "center"

            MDCard:
                orientation: "vertical"
                size_hint: None, None
                size: dp(420), dp(520)
                padding: dp(24)
                spacing: dp(12)
                radius: [18, 18, 18, 18]
                elevation: 0
                md_bg_color: [1, 1, 1, 1]

                MDLabel:
                    text: "Создать аккаунт"
                    font_style: "H5"
                    bold: True
                    halign: "center"

                MDLabel:
                    text: "Заполни данные для входа в систему"
                    halign: "center"
                    theme_text_color: "Secondary"

                MDTextField:
                    id: name
                    hint_text: "ФИО"
                    mode: "rectangle"

                MDTextField:
                    id: email
                    hint_text: "Email"
                    mode: "rectangle"

                MDTextField:
                    id: password
                    hint_text: "Пароль"
                    mode: "rectangle"
                    password: True

                MDTextField:
                    id: password_confirm
                    hint_text: "Подтверждение пароля"
                    mode: "rectangle"
                    password: True

                MDRaisedButton:
                    text: "Зарегистрироваться"
                    on_release: root.on_register()

                MDTextButton:
                    text: "Уже есть аккаунт? Войти"
                    pos_hint: {"center_x": .5}
                    on_release: app.go("login")
'''
Builder.load_string(KV)


class RegisterScreen(BaseScreen):
    _submitting = False

    def on_register(self) -> None:
        if self._submitting:
            return
        name = self.ids.name.text.strip()
        email = self.ids.email.text.strip()
        password = self.ids.password.text
        password_confirm = self.ids.password_confirm.text

        if not name or not email or not password:
            toast("Заполни все обязательные поля")
            return
        if password != password_confirm:
            toast("Пароли не совпадают")
            return

        self._submitting = True
        try:
            self.app.handle_register(name, email, password)
            self.ids.name.text = ""
            self.ids.email.text = ""
            self.ids.password.text = ""
            self.ids.password_confirm.text = ""
            toast("Регистрация успешна")
        except APIError as exc:
            toast(f"Ошибка регистрации: {exc}")
        finally:
            self._submitting = False
