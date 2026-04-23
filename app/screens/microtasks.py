from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem

from app.screens.base import BaseScreen

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
<MicrotasksScreen>:
    name: "microtasks"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")
        MDTopAppBar:
            title: "Микрозадачи и опросы"
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
                    id: task_list
'''
Builder.load_string(KV)


class MicrotasksScreen(BaseScreen):
    def on_pre_enter(self, *args):
        tasks = self.app.load_microtasks()
        surveys = self.app.load_surveys()
        self.ids.task_list.clear_widgets()
        for task in tasks:
            self.ids.task_list.add_widget(OneLineListItem(text=f"Task: {task.get('title', '-')}: {task.get('status', '-') }"))
        for survey in surveys:
            self.ids.task_list.add_widget(
                OneLineListItem(text=f"Survey: {survey.get('title', '-')}: {survey.get('status', '-') }")
            )
