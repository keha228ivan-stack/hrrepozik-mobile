from kivy.lang import Builder
from kivymd.uix.list import ThreeLineListItem

from app.screens.base import BaseScreen

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
<ProgressResultsScreen>:
    name: "progress_results"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")
        MDTopAppBar:
            title: "Результаты и прогресс"
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
