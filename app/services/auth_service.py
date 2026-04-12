from app.models.user import User
from app.services.api_client import APIClient


class AuthService:
    def __init__(self, api: APIClient) -> None:
        self.api = api

    def login(self, email: str, password: str) -> str:
        data = self.api.request("POST", "/api/auth/login", json={"email": email, "password": password})
        return data["access_token"]

    def register(self, name: str, email: str, password: str) -> str:
        data = self.api.request(
            "POST",
            "/api/auth/register",
            json={"name": name, "email": email, "password": password},
        )
        return data["access_token"]

    def me(self) -> User:
        data = self.api.request("GET", "/api/auth/me")
        return User.model_validate(data)
