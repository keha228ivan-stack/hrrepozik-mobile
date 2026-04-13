try:
    from app.app import HRLMSApp
except ModuleNotFoundError as exc:
    missing = exc.name or "dependency"
    print(f"Missing dependency: {missing}. Install requirements with: pip install -r requirements.txt")
    raise


if __name__ == "__main__":
    HRLMSApp().run()
