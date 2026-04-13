from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem

from app.screens.base import BaseScreen

KV = '''
<MicrotasksScreen>:
    name: "microtasks"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Microtasks & Surveys"
            left_action_items: [["home", lambda x: app.go_main_menu()]]
        ScrollView:
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
