from typing import Optional

from app.domain.ports.book_repository import BookRepository
from app.domain.models.book import BookModel
from app.logging.logging import logging


class GetBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book_id: int) -> Optional[BookModel]:
        logging.debug(
            f"Getting book by id: {book_id} from GetBook use case...")
        return self.repository.find_by_id(book_id)
