from datetime import datetime
from app.models.compat import BaseModel


class AppNotification(BaseModel):
    id: int
    title: str
    message: str
    created_at: datetime
    read: bool = False
    type: str = "general"
