from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
<SettingsScreen>:
    name: "settings"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(12)
        MDTopAppBar:
            title: "Settings"
            left_action_items: [["home", lambda x: app.go_main_menu()]]
        MDLabel:
            text: "Settings / Offline"
        MDLabel:
            id: offline_info
            text: "Downloaded files: 0"
        MDRaisedButton:
            text: "Sync pending changes"
            on_release: app.flush_sync()
'''
Builder.load_string(KV)


class SettingsScreen(BaseScreen):
    def on_pre_enter(self, *args):
        self.ids.offline_info.text = f"Downloaded files: {self.app.downloaded_total()}"
