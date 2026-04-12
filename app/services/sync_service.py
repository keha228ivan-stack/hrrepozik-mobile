from app.services.course_service import CourseService
from app.storage.cache_store import CacheStore
from app.utils.logger import get_logger


class SyncService:
    def __init__(self, cache: CacheStore, course_service: CourseService) -> None:
        self.cache = cache
        self.course_service = course_service
        self._log = get_logger("sync")

    def queue_progress(self, course_id: int, progress: int) -> None:
        self.cache.enqueue_sync_action({"type": "course_progress", "course_id": course_id, "progress": progress})

    def flush(self) -> None:
        queue = self.cache.pull_sync_queue()
        if not queue:
            return
        failed: list[dict] = []
        for action in queue:
            try:
                if action["type"] == "course_progress":
                    self.course_service.update_progress(action["course_id"], action["progress"])
            except Exception:
                self._log.exception("Failed to sync action")
                failed.append(action)
        self.cache.set("sync_queue", {"items": failed})
