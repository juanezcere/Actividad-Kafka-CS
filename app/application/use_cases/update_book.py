from app.domain.models.book import BookModel
from app.domain.ports.book_repository import BookRepository
from app.logging.logging import logging


class UpdateBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book_id: int, title: str, author: str, pages: int, description: str, rating: int) -> BookModel:
        existing_book = self.repository.find_by_id(book_id)
        if not existing_book:
            logging.error(f"The book with ID {book_id} was not found.")
            raise Exception(f"The book with ID {book_id} was not found.")
        updated_book = BookModel(
            id=book_id,
            title=title,
            author=author,
            pages=pages,
            description=description,
            rating=rating
        )
        logging.debug(
            f"Updating book: {updated_book} from UpdateBook use case...")
        return self.repository.save(updated_book)
