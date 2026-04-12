from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    api_base_url: str = os.getenv("HRLMS_API_BASE_URL", "https://api.example.com")
    api_timeout_sec: float = float(os.getenv("HRLMS_API_TIMEOUT", "15"))
    environment: str = os.getenv("HRLMS_ENV", "dev")


settings = Settings()
