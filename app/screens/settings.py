from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
<SettingsScreen>:
    name: "settings"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(12)
        MDLabel:
            text: "Settings / Offline"
        MDRaisedButton:
            text: "Sync pending changes"
            on_release: app.flush_sync()
'''
Builder.load_string(KV)


class SettingsScreen(BaseScreen):
    pass
