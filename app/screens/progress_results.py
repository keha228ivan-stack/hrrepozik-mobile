from kivy.lang import Builder
from kivymd.uix.list import ThreeLineListItem

from app.screens.base import BaseScreen

KV = '''
<ProgressResultsScreen>:
    name: "progress_results"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Results & Progress"
            left_action_items: [["home", lambda x: app.go_main_menu()]]
        ScrollView:
            MDList:
                id: list
'''
Builder.load_string(KV)


class ProgressResultsScreen(BaseScreen):
    def on_pre_enter(self, *args):
        self.app.load_learning_data()
        self.ids.list.clear_widgets()
        for item in self.app.state.test_results:
            self.ids.list.add_widget(
                ThreeLineListItem(
                    text=f"Test: {item.get('title', '-')}",
                    secondary_text=f"Score: {item.get('score', '-')}",
                    tertiary_text=f"Status: {'Passed' if item.get('passed') else 'In progress'}",
                )
            )
        for item in self.app.state.assignment_results:
            self.ids.list.add_widget(
                ThreeLineListItem(
                    text=f"Assignment: {item.get('title', '-')}",
                    secondary_text=f"Grade: {item.get('grade', '-')}",
                    tertiary_text=f"Feedback: {item.get('feedback', '-')}",
                )
            )
