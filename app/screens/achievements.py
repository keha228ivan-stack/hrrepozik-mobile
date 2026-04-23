from kivy.lang import Builder
from kivymd.uix.list import TwoLineListItem

from app.screens.base import BaseScreen

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
<AchievementsScreen>:
    name: "achievements"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")
        MDTopAppBar:
            title: "Достижения"
            left_action_items: [["arrow-left", lambda x: app.route_by_role()]]
            right_action_items: [["home-outline", lambda x: app.route_by_role()]]
        ScrollView:
            MDCard:
                orientation: "vertical"
                radius: [16, 16, 16, 16]
                elevation: 0
                md_bg_color: [1, 1, 1, 1]
                padding: "12dp"
                size_hint: .96, None
                adaptive_height: True
                pos_hint: {"center_x": .5}
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
