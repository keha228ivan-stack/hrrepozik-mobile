from kivy.lang import Builder
from kivymd.toast import toast

from app.screens.base import BaseScreen
from app.services.api_client import APIError

KV = '''
#:import dp kivy.metrics.dp
<LoginScreen>:
    name: "login"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(12)
        MDLabel:
            text: "HR LMS Login"
            halign: "center"
            font_style: "H5"
        MDTextField:
            id: email
            hint_text: "Email"
        MDTextField:
            id: password
            hint_text: "Password"
            password: True
        MDRaisedButton:
            text: "Login"
            on_release: root.on_login()
        MDTextButton:
            text: "No account? Register"
            on_release: app.go("register")
'''
Builder.load_string(KV)


class LoginScreen(BaseScreen):
    def on_login(self) -> None:
        email = self.ids.email.text.strip()
        password = self.ids.password.text
        try:
            self.app.handle_login(email, password)
        except APIError as exc:
            toast(f"Login failed: {exc}")
