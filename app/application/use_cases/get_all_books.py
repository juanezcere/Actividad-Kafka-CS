from typing import List

from app.domain.ports.book_repository import BookRepository
from app.domain.models.book import BookModel


class GetAllBooks:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self) -> List[BookModel]:
        return self.repository.find_all()
