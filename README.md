# HR + LMS Mobile (Kivy/KivyMD)

Production-oriented mobile client scaffold for an existing HR+LMS backend.

## Architecture

- `app/screens/`: UI screens (login, role dashboards, courses, employees, profile, notifications, settings).
- `app/widgets/`: reusable widgets (course list items).
- `app/services/`: API client, auth, courses, employees, notifications, sync queue, push stub.
- `app/models/`: strongly typed domain models (Pydantic).
- `app/storage/`: secure token storage and offline cache/sync queue.
- `app/state/`: centralized application state store.
- `app/utils/`: logging and helper utilities.

Implemented modules:
- Authorization / account / session / profile edit
- Employee dashboard, courses, search+filters, progress+results, notifications, microtasks+surveys, achievements+certificates
- Manager dashboard, employees, course assignment, analytics reports
- Offline cache, offline content storage, deferred sync queue, realtime refresh polling

## API integration placeholders

Update endpoints and payload adapters in:
- `app/services/auth_service.py`
- `app/services/course_service.py`
- `app/services/employee_service.py`
- `app/services/notification_service.py`

Base URL and timeout are configurable via env vars:
- `HRLMS_API_BASE_URL`
- `HRLMS_API_TIMEOUT`
- `HRLMS_ENV`
- `HRLMS_TRUST_ENV` (set `0` to ignore system proxy variables)

If `HRLMS_API_BASE_URL` is left as default (`https://api.example.com`), auth works in local offline mode using SQLite.

## Offline and sync

- Course/profile caches are written to `offline_cache.json`.
- Failed progress updates are queued in `sync_queue` and replayed from Settings.
- Local SQLite database `hr_lms_mobile.db` stores users and sync-ready entities (`users`, `courses`, `notifications`, `sync_actions`).
- The schema includes `external_id` fields to map records with site/desktop backend IDs during future bidirectional sync.

## Notifications

- API notifications are supported via `NotificationService`.
- `PushService` is a stub integration point for Firebase/APNS bridge.

## Run

Python: **3.10–3.13**. Python **3.14+** is not supported in this project because Kivy wheel build fails on typical Windows setup without native C/C++ toolchain.

```bash
pip install -r requirements.txt
python main.py
```

Windows quick start:
```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

