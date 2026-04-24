from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
#:import get_color_from_hex kivy.utils.get_color_from_hex
<SettingsScreen>:
    name: "settings"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")
        padding: dp(12)
        MDTopAppBar:
            title: "Настройки"
            left_action_items: [["arrow-left", lambda x: app.route_by_role()]]
            right_action_items: [["home-outline", lambda x: app.route_by_role()]]
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
