from app.models.notification import AppNotification
from app.services.api_client import APIClient


class NotificationService:
    def __init__(self, api: APIClient) -> None:
        self.api = api

    def list_notifications(self) -> list[AppNotification]:
        payload = self.api.request("GET", "/api/notifications")
        return [AppNotification.model_validate(item) for item in payload.get("items", [])]

    def mark_read(self, notification_id: int) -> None:
        self.api.request("POST", f"/api/notifications/{notification_id}/read")
