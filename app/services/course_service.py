from app.models.course import Course
from app.services.api_client import APIClient


class CourseService:
    def __init__(self, api: APIClient) -> None:
        self.api = api

    def list_courses(self, query: dict | None = None) -> list[Course]:
        payload = self.api.request("POST", "/api/courses/search", json=query or {})
        return [Course.model_validate(item) for item in payload.get("items", [])]

    def get_course_detail(self, course_id: int) -> dict:
        return self.api.request("GET", f"/api/courses/{course_id}")

    def update_progress(self, course_id: int, progress: int) -> None:
        self.api.request("POST", f"/api/courses/{course_id}/progress", json={"progress": progress})
