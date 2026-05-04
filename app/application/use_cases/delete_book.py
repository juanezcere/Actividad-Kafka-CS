from app.domain.ports.book_repository import BookRepository


class DeleteBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book_id: int) -> bool:
        return self.repository.delete(book_id)
