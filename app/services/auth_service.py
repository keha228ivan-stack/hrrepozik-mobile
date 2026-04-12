from app.models.user import User
from app.services.api_client import APIClient, APIError
from app.storage.local_db import LocalDatabase


class AuthService:
    def __init__(self, api: APIClient, local_db: LocalDatabase) -> None:
        self.api = api
        self.local_db = local_db
        self._active_token: str | None = None

    def set_active_token(self, token: str | None) -> None:
        self._active_token = token

    @staticmethod
    def _validate_registration(name: str, email: str, password: str) -> None:
        if not name.strip():
            raise APIError("Name is required")
        if "@" not in email or "." not in email:
            raise APIError("Invalid email format")
        if len(password) < 6:
            raise APIError("Password must contain at least 6 characters")

    def login(self, email: str, password: str) -> str:
        try:
            data = self.api.request("POST", "/api/auth/login", json={"email": email, "password": password})
            token = data["access_token"]
        except APIError:
            user = self.local_db.verify_user(email, password)
            if not user:
                raise APIError("Invalid credentials")
            token = f"local:{user.id}"
        self._active_token = token
        return token

    def register(self, name: str, email: str, password: str) -> str:
        self._validate_registration(name, email, password)
        existing = self.local_db.get_user_by_email(email)
        if existing:
            raise APIError("User with this email already exists")
        try:
            data = self.api.request(
                "POST",
                "/api/auth/register",
                json={"name": name, "email": email, "password": password},
            )
            token = data["access_token"]
        except APIError:
            user = self.local_db.create_user(name=name, email=email, password=password, role="employee")
            token = f"local:{user.id}"
        self._active_token = token
        return token

    def me(self) -> User:
        if self._active_token and self._active_token.startswith("local:"):
            user_id = int(self._active_token.split(":", 1)[1])
            user = self.local_db.get_user_by_id(user_id)
            if not user:
                raise APIError("Local user session not found")
            return user
        data = self.api.request("GET", "/api/auth/me")
        user = User.model_validate(data)
        return user
