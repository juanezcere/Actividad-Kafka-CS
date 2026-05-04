import sqlite3
from typing import List

from app.domain.models.log import LogModel
from app.domain.ports.log_repository import LogRepository
from app.logging.logging import logging


class SQLiteLogRepository(LogRepository):
    def __init__(self, db_path: str = "data/logs.db"):
        self.db_path = db_path
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        logging.debug("Creating logs table...")
        query = """
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            topic TEXT NOT NULL,
            level INTEGER NOT NULL,
            message TEXT NOT NULL
        )
        """
        with self._get_connection() as conn:
            conn.execute(query)

    def save(self, log: LogModel) -> LogModel:
        logging.debug(f"Saving log: {log}, from SQLite log repository")
        query = """
        INSERT INTO logs (timestamp, topic, level, message) 
        VALUES (?, ?, ?, ?)
        """
        with self._get_connection() as conn:
            parameters = (
                log.timestamp,
                log.topic,
                log.level,
                log.message
            )
            conn.execute(query, parameters)
        return log

    def find_all(self) -> List[LogModel]:
        logging.debug("Finding all logs from SQLite log repository...")
        query = "SELECT id, timestamp, topic, level, message FROM logs ORDER BY timestamp DESC"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            rows = cursor.execute(query).fetchall()
            return [LogModel(*row) for row in rows]
