from pydantic import BaseModel


class TestResult(BaseModel):
    course_id: int
    title: str
    score: float
    passed: bool


class AssignmentResult(BaseModel):
    course_id: int
    title: str
    grade: str | None = None
    feedback: str | None = None


class Achievement(BaseModel):
    id: int
    title: str
    kind: str
    awarded_at: str | None = None


class Certificate(BaseModel):
    id: int
    title: str
    url: str | None = None


class MicroTask(BaseModel):
    id: int
    title: str
    status: str


class Survey(BaseModel):
    id: int
    title: str
    status: str
