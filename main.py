import sys


def _exit_with_message(message: str) -> None:
    print(message)
    raise SystemExit(1)


def _ensure_supported_python() -> None:
    if sys.version_info < (3, 10):
        _exit_with_message(
            "Требуется Python 3.10+ для запуска приложения. "
            "Обнови интерпретатор и установи зависимости: pip install -r requirements.txt"
        )


if sys.version_info >= (3, 14):
    _exit_with_message(
        "Python 3.14+ пока не поддерживается для этого приложения (Kivy wheel недоступен).\n"
        "Используй Python 3.10–3.13, затем: pip install -r requirements.txt"
    )


try:
    _ensure_supported_python()
    from app.app import HRLMSApp
except ModuleNotFoundError as exc:
    missing = exc.name or "dependency"
    _exit_with_message(
        f"Missing dependency: {missing}. Install requirements with: pip install -r requirements.txt"
    )


if __name__ == "__main__":
    HRLMSApp().run()
