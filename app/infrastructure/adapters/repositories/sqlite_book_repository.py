import sqlite3
from typing import List, Optional

from app.domain.models.book import BookModel
from app.domain.ports.book_repository import BookRepository


class SQLiteBookRepository(BookRepository):
    def __init__(self, db_path: str = "data/library.db"):
        self.db_path = db_path
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            pages INTEGER,
            description TEXT,
            rating INTEGER
        )
        """
        with self._get_connection() as conn:
            conn.execute(query)

    def save(self, book: BookModel) -> BookModel:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            if book.id is None:
                query = "INSERT INTO books (title, author, pages, description, rating) VALUES (?, ?, ?, ?, ?)"
                parameters = (book.title, book.author, book.pages,
                              book.description, book.rating)
                cursor.execute(query, parameters)
                book.id = cursor.lastrowid
            else:
                query = "UPDATE books SET title=?, author=?, pages=?, description=?, rating=? WHERE id=?"
                parameters = (book.title, book.author, book.pages,
                              book.description, book.rating, book.id)
                cursor.execute(query, parameters)
            return book

    def find_all(self) -> List[BookModel]:
        query = "SELECT id, title, author, pages, description, rating FROM books"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            rows = cursor.execute(query).fetchall()
            return [BookModel(*row) for row in rows]

    def find_by_id(self, book_id: int) -> Optional[BookModel]:
        query = "SELECT id, title, author, pages, description, rating FROM books WHERE id = ?"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            row = cursor.execute(query, (book_id,)).fetchone()
            if row:
                return BookModel(*row)
            return None

    def delete(self, book_id: int) -> bool:
        query = "DELETE FROM books WHERE id = ?"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, (book_id,))
            return result.rowcount > 0
        return False
