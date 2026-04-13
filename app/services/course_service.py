from app.models.course import Course
from app.services.api_client import APIClient


class CourseService:
    def __init__(self, api: APIClient) -> None:
        self.api = api

    def list_courses(self, query: dict | None = None) -> list[Course]:
        payload = self.api.request("POST", "/api/courses/search", json=query or {})
        return [Course.model_validate(item) for item in payload.get("items", [])]

    def assigned_courses(self, user_id: int) -> list[Course]:
        payload = self.api.request("GET", f"/api/users/{user_id}/courses")
        return [Course.model_validate(item) for item in payload.get("items", [])]

    def get_course_detail(self, course_id: int) -> dict:
        return self.api.request("GET", f"/api/courses/{course_id}")

    def course_materials(self, course_id: int) -> dict:
        return self.api.request("GET", f"/api/courses/{course_id}/materials")

    def update_progress(self, course_id: int, progress: int) -> None:
        self.api.request("POST", f"/api/courses/{course_id}/progress", json={"progress": progress})

    def test_results(self) -> list[dict]:
        payload = self.api.request("GET", "/api/learning/tests/results")
        return payload.get("items", [])

    def assignment_results(self) -> list[dict]:
        payload = self.api.request("GET", "/api/learning/assignments/results")
        return payload.get("items", [])

    def achievements(self) -> dict:
        return self.api.request("GET", "/api/learning/achievements")

    def microtasks(self) -> list[dict]:
        payload = self.api.request("GET", "/api/learning/microtasks")
        return payload.get("items", [])

    def surveys(self) -> list[dict]:
        payload = self.api.request("GET", "/api/learning/surveys")
        return payload.get("items", [])

    def submit_microtask(self, task_id: int, answer: str) -> None:
        self.api.request("POST", f"/api/learning/microtasks/{task_id}/submit", json={"answer": answer})

    def submit_survey(self, survey_id: int, answers: dict) -> None:
        self.api.request("POST", f"/api/learning/surveys/{survey_id}/submit", json={"answers": answers})

    def ask_question(self, course_id: int, text: str) -> None:
        self.api.request("POST", f"/api/courses/{course_id}/questions", json={"text": text})
