import sys


def _ensure_supported_python() -> None:
    if sys.version_info >= (3, 14):
        current = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        raise SystemExit(
            "Unsupported Python version for this app: "
            f"{current}. Use Python 3.10–3.13, then run: pip install -r requirements.txt"
        )


try:
    _ensure_supported_python()
    from app.app import HRLMSApp
except ModuleNotFoundError as exc:
    missing = exc.name or "dependency"
    print(f"Missing dependency: {missing}. Install requirements with: pip install -r requirements.txt")
    if missing in {"kivy", "kivymd"} and sys.version_info >= (3, 14):
        print("Detected Python 3.14+, where Kivy/KivyMD are unsupported in this project.")
        print("Please install Python 3.10–3.13 and reinstall dependencies.")
    raise
except SystemExit as exc:
    print(exc)
    raise


if __name__ == "__main__":
    HRLMSApp().run()
