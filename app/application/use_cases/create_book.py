from app.domain.models.book import BookModel
from app.domain.ports.book_repository import BookRepository
from app.logging.logging import logging


class CreateBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, title: str, author: str, pages: int, description: str, rating: int) -> BookModel:
        new_book = BookModel(
            id=None,
            title=title,
            author=author,
            pages=pages,
            description=description,
            rating=rating
        )
        logging.debug(
            f"Creating book: {new_book} from CreateBook use case...")
        return self.repository.save(new_book)
