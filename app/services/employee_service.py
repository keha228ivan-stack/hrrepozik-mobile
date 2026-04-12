from app.models.employee import EmployeeProgress
from app.services.api_client import APIClient


class EmployeeService:
    def __init__(self, api: APIClient) -> None:
        self.api = api

    def list_employees(self, filters: dict | None = None) -> list[EmployeeProgress]:
        payload = self.api.request("POST", "/api/manager/employees/search", json=filters or {})
        return [EmployeeProgress.model_validate(item) for item in payload.get("items", [])]

    def employee_detail(self, user_id: int) -> dict:
        return self.api.request("GET", f"/api/manager/employees/{user_id}")

    def assign_course(self, user_id: int, course_id: int) -> None:
        self.api.request("POST", "/api/manager/assignments", json={"user_id": user_id, "course_id": course_id})
