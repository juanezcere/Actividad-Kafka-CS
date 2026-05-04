from typing import List

from app.domain.ports.book_repository import BookRepository
from app.domain.models.book import BookModel
from app.logging.logging import logging


class GetAllBooks:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self) -> List[BookModel]:
        logging.debug("Getting all books from GetAllBooks use case...")
        return self.repository.find_all()
