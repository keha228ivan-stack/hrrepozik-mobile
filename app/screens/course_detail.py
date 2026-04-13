from kivy.lang import Builder

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
<CourseDetailScreen>:
    name: "course_detail"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(12)
        spacing: dp(8)
        MDLabel:
            id: title
            text: "Course"
            font_style: "H6"
        MDLabel:
            id: description
            text: "Description"
        MDLabel:
            id: materials
            text: "Materials: -"
        MDProgressBar:
            id: progress
            value: 0
            max: 100
        MDRaisedButton:
            text: "Mark +10%"
            on_release: root.bump_progress()
        MDTextField:
            id: question
            hint_text: "Ask question to instructor/team"
        MDRaisedButton:
            text: "Send question"
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
