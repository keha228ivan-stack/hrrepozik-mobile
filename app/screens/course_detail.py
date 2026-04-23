from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
#:import get_color_from_hex kivy.utils.get_color_from_hex
<CourseDetailScreen>:
    name: "course_detail"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")
        MDTopAppBar:
            title: "Детали курса"
            left_action_items: [["arrow-left", lambda x: app.go("course_list")]]
            right_action_items: [["home-outline", lambda x: app.route_by_role()]]

        ScrollView:
            MDCard:
                orientation: "vertical"
                padding: dp(16)
                spacing: dp(10)
                radius: [16, 16, 16, 16]
                elevation: 0
                md_bg_color: [1, 1, 1, 1]
                size_hint: .96, None
                adaptive_height: True
                pos_hint: {"center_x": .5}

                MDLabel:
                    id: title
                    text: "Course"
                    font_style: "H6"
                    bold: True

                MDLabel:
                    id: description
                    text: "Description"
                    theme_text_color: "Secondary"

                MDLabel:
                    id: materials
                    text: "Materials: -"
                    theme_text_color: "Secondary"

                MDProgressBar:
                    id: progress
                    value: 0
                    max: 100

                MDRaisedButton:
                    text: "Отметить +10%"
                    on_release: root.bump_progress()

                MDTextField:
                    id: question
                    hint_text: "Задать вопрос по курсу"
                    mode: "rectangle"

                MDRaisedButton:
                    text: "Отправить вопрос"
                    on_release: root.send_question()
'''
Builder.load_string(KV)


class CourseDetailScreen(BaseScreen):
    course_id: int | None = None

    def on_pre_enter(self, *args):
        course = self.app.get_selected_course()
        if not course:
            return
        self.course_id = course.id
        self.ids.title.text = course.title
        self.ids.description.text = course.description
        self.ids.progress.value = course.progress
        materials = self.app.load_course_materials(course.id)
        self.ids.materials.text = (
            f"Materials: videos={len(materials.get('videos', []))}, docs={len(materials.get('documents', []))}, "
            f"tests={len(materials.get('tests', []))}, assignments={len(materials.get('assignments', []))}"
        )

    def bump_progress(self):
        if self.course_id is None:
            return
        new_value = min(100, int(self.ids.progress.value) + 10)
        self.ids.progress.value = new_value
        self.app.update_course_progress(self.course_id, new_value)

    def send_question(self):
        if self.course_id is None:
            return
        text = self.ids.question.text.strip()
        if not text:
            return
        self.app.ask_course_question(self.course_id, text)
        self.ids.question.text = ""
