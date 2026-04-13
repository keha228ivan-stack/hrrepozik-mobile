from kivy.lang import Builder
from kivymd.uix.list import TwoLineListItem

from app.screens.base import BaseScreen

KV = '''
<AchievementsScreen>:
    name: "achievements"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Achievements"
            left_action_items: [["home", lambda x: app.go_main_menu()]]
        ScrollView:
            MDList:
                id: list
'''
Builder.load_string(KV)


class AchievementsScreen(BaseScreen):
    def on_pre_enter(self, *args):
        self.app.load_learning_data()
        data = self.app.state.achievements
        self.ids.list.clear_widgets()
        for ach in data.get("achievements", []):
            self.ids.list.add_widget(TwoLineListItem(text=ach.get("title", "Achievement"), secondary_text=ach.get("kind", "")))
        for cert in data.get("certificates", []):
            self.ids.list.add_widget(TwoLineListItem(text=cert.get("title", "Certificate"), secondary_text="Certificate"))
