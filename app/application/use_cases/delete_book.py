from app.domain.ports.book_repository import BookRepository
from app.logging.logging import logging


class DeleteBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book_id: int) -> bool:
        logging.debug(
            f"Deleting book by id: {book_id} from DeleteBook use case...")
        return self.repository.delete(book_id)
