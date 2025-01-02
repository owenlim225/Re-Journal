import sqlite3
from pathlib import Path
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.setup_database()

    def setup_database(self):
        """Create SQLite database and table if not exists."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS TextEntries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    timestamp TEXT NOT NULL
                )
            """)
            conn.commit()

    def save_text(self, content: str):
        """Save the text content to the database."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO TextEntries (content, timestamp) VALUES (?, ?)", (content, timestamp))
            conn.commit()
