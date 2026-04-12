from kivy.storage.jsonstore import JsonStore
from platformdirs import user_data_dir
from pathlib import Path


class SecureTokenStore:
    def __init__(self, app_name: str = "hr_lms_mobile") -> None:
        data_dir = Path(user_data_dir(appname=app_name, appauthor="hr_lms"))
        data_dir.mkdir(parents=True, exist_ok=True)
        self._store = JsonStore(str(data_dir / "secure_token.json"))

    def save_token(self, token: str) -> None:
        self._store.put("auth", token=token)

    def get_token(self) -> str | None:
        return self._store.get("auth").get("token") if self._store.exists("auth") else None

    def clear(self) -> None:
        if self._store.exists("auth"):
            self._store.delete("auth")
