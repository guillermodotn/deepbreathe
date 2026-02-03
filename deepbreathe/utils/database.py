"""SQLite database for persisting app data."""

import os
import sqlite3
from pathlib import Path

from kivy.utils import platform


def get_data_dir() -> Path:
    """Get the platform-appropriate data directory.

    In development mode (DEEPBREATHE_DEV=1), uses the project directory.
    Otherwise uses the platform-appropriate location:
    - Linux/Desktop: ~/.local/share/deepbreathe (or XDG_DATA_HOME)
    - Android: app storage path
    - iOS: documents directory
    """
    # Development mode: use project directory
    if os.environ.get("DEEPBREATHE_DEV"):
        return Path(__file__).parent.parent.parent

    if platform == "android":
        from android.storage import app_storage_path  # type: ignore

        return Path(app_storage_path())
    elif platform == "ios":
        from pyobjus import autoclass  # type: ignore

        ns_search = autoclass("NSSearchPathForDirectoriesInDomains")
        docs = ns_search(9, 1, True).objectAtIndex_(0)
        return Path(docs)
    else:
        # Desktop: use XDG data home or fallback
        xdg_data = os.environ.get("XDG_DATA_HOME")
        if xdg_data:
            data_dir = Path(xdg_data) / "deepbreathe"
        else:
            data_dir = Path.home() / ".local" / "share" / "deepbreathe"
        data_dir.mkdir(parents=True, exist_ok=True)
        return data_dir


def get_db_path() -> Path:
    """Get the path to the SQLite database file."""
    return get_data_dir() / "deepbreathe.db"


def get_connection() -> sqlite3.Connection:
    """Get a connection to the database."""
    conn = sqlite3.connect(str(get_db_path()))
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize the database schema."""
    conn = get_connection()
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                training_type TEXT NOT NULL,
                score REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_scores_training_type
            ON scores (training_type)
        """)
        conn.commit()
    finally:
        conn.close()


def save_score(training_type: str, score: float) -> None:
    """Save a score to the database.

    Args:
        training_type: The type of training (e.g., 'free', 'o2', 'co2')
        score: The score/time achieved in seconds
    """
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO scores (training_type, score) VALUES (?, ?)",
            (training_type, score),
        )
        conn.commit()
    finally:
        conn.close()


def get_best_score(training_type: str) -> float | None:
    """Get the best (highest) score for a training type.

    Args:
        training_type: The type of training (e.g., 'free', 'o2', 'co2')

    Returns:
        The best score in seconds, or None if no scores exist
    """
    conn = get_connection()
    try:
        cursor = conn.execute(
            "SELECT MAX(score) as best FROM scores WHERE training_type = ?",
            (training_type,),
        )
        row = cursor.fetchone()
        return row["best"] if row and row["best"] is not None else None
    finally:
        conn.close()


# Initialize database on module import
init_db()
