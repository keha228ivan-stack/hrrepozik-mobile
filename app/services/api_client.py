from __future__ import annotations

from typing import Any
import httpx

from app.config import settings
from app.utils.logger import get_logger


class APIError(Exception):
    pass


class UnauthorizedError(APIError):
    pass


class APIClient:
    def __init__(self) -> None:
        self._log = get_logger("api")
        self._token: str | None = None
        self._client = httpx.Client(base_url=settings.api_base_url, timeout=settings.api_timeout_sec)

    def set_token(self, token: str | None) -> None:
        self._token = token

    def _headers(self) -> dict[str, str]:
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        return headers

    def request(self, method: str, path: str, *, json: dict | None = None, retry: int = 1) -> Any:
        last_exc: Exception | None = None
        for _ in range(retry + 1):
            try:
                resp = self._client.request(method, path, json=json, headers=self._headers())
                if resp.status_code == 401:
                    raise UnauthorizedError("Token invalid or expired")
                if resp.status_code >= 400:
                    raise APIError(f"HTTP {resp.status_code}: {resp.text}")
                if not resp.text:
                    return None
                return resp.json()
            except httpx.RequestError as exc:
                self._log.exception("Network error while calling %s %s", method, path)
                last_exc = exc
            except ValueError as exc:
                raise APIError("Invalid JSON response") from exc
        raise APIError(f"Network unavailable: {last_exc}")
