class PushService:
    def initialize(self) -> None:
        # Integration point for Firebase/APNS bridge for Kivy.
        return

    def subscribe_user(self, user_id: int) -> None:
        return

    def schedule_local_reminder(self, title: str, body: str, when_iso: str) -> None:
        # Hook for platform-specific local notifications (plyer/android alarm manager).
        return
