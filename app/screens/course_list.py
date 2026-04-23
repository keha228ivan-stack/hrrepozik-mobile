from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
#:import get_color_from_hex kivy.utils.get_color_from_hex
<CourseListScreen>:
    name: "course_list"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")
        MDTopAppBar:
            title: "Обучение"
            left_action_items: [["arrow-left", lambda x: app.route_by_role()]]
            right_action_items: [["home-outline", lambda x: app.route_by_role()]]

        MDCard:
            orientation: "vertical"
            radius: [16, 16, 16, 16]
            elevation: 0
            md_bg_color: [1, 1, 1, 1]
            padding: dp(16)
            spacing: dp(10)
            size_hint: 1, 1
            pos_hint: {"center_x": .5, "center_y": .5}

            MDTextField:
                id: query
                hint_text: "Поиск курса"
                mode: "rectangle"
                on_text_validate: root.apply_filter()

            MDTextField:
                id: status
                hint_text: "Фильтр: active/completed/overdue"
                mode: "rectangle"
                on_text_validate: root.apply_filter()

            ScrollView:
                MDList:
                    id: list
'''
Builder.load_string(KV)


class CourseListScreen(BaseScreen):
    def on_pre_enter(self, *args):
        self.render(self.app.state.courses)

    def apply_filter(self):
        q = self.ids.query.text.lower().strip()
        status = self.ids.status.text.lower().strip()
        filtered = [c for c in self.app.state.courses if q in c.title.lower()]
        if status:
            filtered = [c for c in filtered if c.status.lower() == status]
        self.render(filtered)

    def render(self, courses):
        self.ids.list.clear_widgets()
        for course in courses:
            self.ids.list.add_widget(self.app.widgets.course_item(course, "course_detail"))
