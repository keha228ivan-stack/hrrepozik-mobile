from datetime import datetime, timezone
from kivy.storage.jsonstore import JsonStore
from platformdirs import user_data_dir
from pathlib import Path


class CacheStore:
    def __init__(self, app_name: str = "hr_lms_mobile") -> None:
        data_dir = Path(user_data_dir(appname=app_name, appauthor="hr_lms"))
        data_dir.mkdir(parents=True, exist_ok=True)
        self._store = JsonStore(str(data_dir / "offline_cache.json"))

    def set(self, key: str, payload: dict) -> None:
        self._store.put(key, payload=payload, updated_at=datetime.now(timezone.utc).isoformat())

    def get(self, key: str) -> dict | None:
        if not self._store.exists(key):
            return None
        return self._store.get(key).get("payload")

    def enqueue_sync_action(self, action: dict) -> None:
        queue = self.get("sync_queue") or {"items": []}
        queue["items"].append(action)
        self.set("sync_queue", queue)

    def pull_sync_queue(self) -> list[dict]:
        queue = self.get("sync_queue") or {"items": []}
        return queue.get("items", [])

    def clear_sync_queue(self) -> None:
        self.set("sync_queue", {"items": []})
