from kivy.lang import Builder
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText

from app.screens.base import BaseScreen
from app.services.api_client import APIError

KV = '''
<RegisterScreen>:
    name: "register"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(12)
        MDLabel:
            text: "Create account"
            halign: "center"
            font_style: "H5"
        MDTextField:
            id: name
            hint_text: "Full name"
        MDTextField:
            id: email
            hint_text: "Email"
        MDTextField:
            id: password
            hint_text: "Password"
            password: True
        MDRaisedButton:
            text: "Register"
            on_release: root.on_register()
'''
Builder.load_string(KV)


class RegisterScreen(BaseScreen):
    def on_register(self) -> None:
        try:
            self.app.handle_register(self.ids.name.text.strip(), self.ids.email.text.strip(), self.ids.password.text)
        except APIError as exc:
            MDSnackbar(MDSnackbarText(text=f"Registration failed: {exc}")).open()
