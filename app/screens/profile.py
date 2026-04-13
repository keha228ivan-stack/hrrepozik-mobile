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
        MDTopAppBar:
            title: "Profile"
            left_action_items: [["arrow-left", lambda x: root.back_to_dashboard()]]
        MDLabel:
            id: name
            text: "Name:"
        MDTextField:
            id: name_input
            hint_text: "Edit name"
        MDLabel:
            id: email
            text: "Email:"
        MDLabel:
            id: role
            text: "Role:"
        MDTextField:
            id: department_input
            hint_text: "Department"
        MDRaisedButton:
            text: "Save profile"
            on_release: root.save_profile()
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
        self.ids.name_input.text = user.name
        self.ids.email.text = f"Email: {user.email}"
        self.ids.role.text = f"Role: {user.role}"
        self.ids.department_input.text = user.department or ""

    def save_profile(self):
        self.app.update_profile(
            {"name": self.ids.name_input.text.strip(), "department": self.ids.department_input.text.strip()}
        )

    def back_to_dashboard(self):
        self.app.route_by_role()
