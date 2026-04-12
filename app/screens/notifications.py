from kivy.lang import Builder
from kivymd.uix.list import TwoLineListItem

from app.screens.base import BaseScreen

KV = '''
<NotificationsScreen>:
    name: "notifications"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Notifications"
        ScrollView:
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
