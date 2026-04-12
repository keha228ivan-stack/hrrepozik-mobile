from kivymd.uix.list import ThreeLineListItem


class CourseListItem(ThreeLineListItem):
    def __init__(self, course, on_open, **kwargs):
        super().__init__(
            text=course.title,
            secondary_text=f"Status: {course.status} | Progress: {course.progress}%",
            tertiary_text=f"Deadline: {course.deadline.isoformat() if course.deadline else '-'}",
            **kwargs,
        )
        self.bind(on_release=lambda *_: on_open(course.id))
