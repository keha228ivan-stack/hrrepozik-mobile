import sys
import traceback


def _exit_with_message(message: str) -> None:
    print(message)
    raise SystemExit(1)


def _pause_before_exit() -> None:
    if sys.platform.startswith("win") and sys.stdin and sys.stdin.isatty():
        try:
            input("\nНажми Enter для выхода...")
        except EOFError:
            pass


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
    if missing == "pydantic_core._pydantic_core":
        _exit_with_message(
            "Missing dependency: pydantic_core._pydantic_core.\n"
            "Переустанови зависимости в активном venv:\n"
            "python -m pip install --upgrade pip\n"
            "python -m pip install --force-reinstall pydantic-core pydantic\n"
            "python -m pip install -r requirements.txt"
        )
    _exit_with_message(
        f"Missing dependency: {missing}. Install requirements with: pip install -r requirements.txt"
    )


if __name__ == "__main__":
    try:
        HRLMSApp().run()
    except Exception:
        print("Приложение завершилось с ошибкой. Traceback ниже:\n")
        traceback.print_exc()
        _pause_before_exit()
        raise
