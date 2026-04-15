import sys

try:
    _ensure_supported_python()
    from app.app import HRLMSApp
except ModuleNotFoundError as exc:
    missing = exc.name or "dependency"
    print(f"Missing dependency: {missing}. Install requirements with: pip install -r requirements.txt")
    if missing in {"kivy", "kivymd"} and sys.version_info >= (3, 14):
        print("Python 3.14 detected: this project uses nightly Kivy/KivyMD from GitHub for 3.14.")
        print("Please run: pip install --upgrade pip setuptools wheel && pip install -r requirements.txt")
    raise


if __name__ == "__main__":
    HRLMSApp().run()
