from typing import Optional

from app.domain.ports.book_repository import BookRepository
from app.domain.models.book import BookModel


class GetBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book_id: int) -> Optional[BookModel]:
        return self.repository.find_by_id(book_id)
