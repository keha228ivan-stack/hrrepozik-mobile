from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    email: str
    role: str = Field(pattern=r"^(employee|manager)$")
    avatar_url: str | None = None
    department: str | None = None
