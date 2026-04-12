from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
<ProfileScreen>:
    name: "profile"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(16)
        spacing: dp(8)
        MDLabel:
            id: name
            text: "Name:"
        MDLabel:
            id: email
            text: "Email:"
        MDLabel:
            id: role
            text: "Role:"
        MDRaisedButton:
            text: "Logout"
            on_release: app.logout()
'''
Builder.load_string(KV)


class ProfileScreen(BaseScreen):
    def on_pre_enter(self, *args):
        user = self.app.state.user
        if not user:
            return
        self.ids.name.text = f"Name: {user.name}"
        self.ids.email.text = f"Email: {user.email}"
        self.ids.role.text = f"Role: {user.role}"
