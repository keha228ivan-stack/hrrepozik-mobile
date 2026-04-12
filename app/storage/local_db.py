from __future__ import annotations

import hashlib
import sqlite3
from pathlib import Path

from platformdirs import user_data_dir

from app.models.user import User


class LocalDatabase:
    def __init__(self, app_name: str = "hr_lms_mobile") -> None:
        data_dir = Path(user_data_dir(appname=app_name, appauthor="hr_lms"))
        data_dir.mkdir(parents=True, exist_ok=True)
        self.db_path = data_dir / "hr_lms_mobile.db"
        self._init_schema()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_schema(self) -> None:
        with self._connect() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    external_id INTEGER,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    role TEXT NOT NULL CHECK(role IN ('employee', 'manager')),
                    password_hash TEXT NOT NULL,
                    avatar_url TEXT,
                    department TEXT,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                );

                CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    external_id INTEGER,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT,
                    deadline TEXT,
                    progress INTEGER DEFAULT 0,
                    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
                );

                CREATE TABLE IF NOT EXISTS notifications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    external_id INTEGER,
                    title TEXT NOT NULL,
                    message TEXT NOT NULL,
                    read INTEGER DEFAULT 0,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                );

                CREATE TABLE IF NOT EXISTS sync_actions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    action_type TEXT NOT NULL,
                    payload TEXT NOT NULL,
                    status TEXT DEFAULT 'pending',
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                );
                """
            )

    @staticmethod
    def _hash_password(password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def create_user(self, *, name: str, email: str, password: str, role: str = "employee") -> User:
        password_hash = self._hash_password(password)
        with self._connect() as conn:
            cur = conn.execute(
                "INSERT INTO users(name, email, role, password_hash) VALUES (?, ?, ?, ?)",
                (name, email.lower().strip(), role, password_hash),
            )
            user_id = cur.lastrowid
        return User(id=user_id, name=name, email=email.lower().strip(), role=role)

    def get_user_by_email(self, email: str) -> User | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT id, name, email, role, avatar_url, department FROM users WHERE email = ?",
                (email.lower().strip(),),
            ).fetchone()
        if not row:
            return None
        return User(
            id=row["id"],
            name=row["name"],
            email=row["email"],
            role=row["role"],
            avatar_url=row["avatar_url"],
            department=row["department"],
        )

    def verify_user(self, email: str, password: str) -> User | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT id, name, email, role, avatar_url, department, password_hash FROM users WHERE email = ?",
                (email.lower().strip(),),
            ).fetchone()
        if not row:
            return None
        if row["password_hash"] != self._hash_password(password):
            return None
        return User(
            id=row["id"],
            name=row["name"],
            email=row["email"],
            role=row["role"],
            avatar_url=row["avatar_url"],
            department=row["department"],
        )

    def get_user_by_id(self, user_id: int) -> User | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT id, name, email, role, avatar_url, department FROM users WHERE id = ?",
                (user_id,),
            ).fetchone()
        if not row:
            return None
        return User(
            id=row["id"],
            name=row["name"],
            email=row["email"],
            role=row["role"],
            avatar_url=row["avatar_url"],
            department=row["department"],
        )
