from kivy.lang import Builder
from kivymd.uix.list import TwoLineListItem

from app.screens.base import BaseScreen

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
<NotificationsScreen>:
    name: "notifications"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")
        MDTopAppBar:
            title: "Уведомления"
            left_action_items: [["arrow-left", lambda x: app.route_by_role()]]
            right_action_items: [["home-outline", lambda x: app.route_by_role()], ["logout", lambda x: app.logout()]]
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


class NotificationsScreen(BaseScreen):
    def on_pre_enter(self, *args):
        self.app.load_notifications()
        self.ids.list.clear_widgets()
        for note in self.app.state.notifications:
            self.ids.list.add_widget(TwoLineListItem(text=note.title, secondary_text=note.message))
