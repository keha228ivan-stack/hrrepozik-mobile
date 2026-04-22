from datetime import datetime
from app.models.compat import BaseModel


class Course(BaseModel):
    id: int
    title: str
    description: str = ""
    author: str | None = None
    duration_minutes: int | None = None
    status: str
    deadline: datetime | None = None
    progress: int = 0
    category: str | None = None
    level: str | None = None


class CourseModule(BaseModel):
    id: int
    title: str
    completed: bool = False
