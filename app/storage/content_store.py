from pathlib import Path
from platformdirs import user_data_dir


class OfflineContentStore:
    def __init__(self, app_name: str = "hr_lms_mobile") -> None:
        self.root = Path(user_data_dir(appname=app_name, appauthor="hr_lms")) / "downloads"
        self.root.mkdir(parents=True, exist_ok=True)

    def mark_downloaded(self, course_id: int, content_type: str, filename: str, data: bytes) -> str:
        folder = self.root / f"course_{course_id}" / content_type
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / filename
        path.write_bytes(data)
        return str(path)

    def list_downloaded(self, course_id: int) -> list[str]:
        folder = self.root / f"course_{course_id}"
        if not folder.exists():
            return []
        return [str(p) for p in folder.rglob("*") if p.is_file()]

    def list_all_downloaded(self) -> list[str]:
        return [str(p) for p in self.root.rglob("*") if p.is_file()]
