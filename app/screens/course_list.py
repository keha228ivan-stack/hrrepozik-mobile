from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
<CourseListScreen>:
    name: "course_list"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Courses"
            left_action_items: [["home", lambda x: app.go_main_menu()]]
        MDTextField:
            id: query
            hint_text: "Search"
            on_text_validate: root.apply_filter()
        MDTextField:
            id: status
            hint_text: "Status filter (active/completed/overdue)"
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
