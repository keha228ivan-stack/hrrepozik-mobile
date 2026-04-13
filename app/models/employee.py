from pydantic import BaseModel


class EmployeeProgress(BaseModel):
    user_id: int
    name: str
    department: str | None = None
    avg_progress: int = 0
    completed_courses: int = 0
    overdue_courses: int = 0
    kpi: float | None = None
