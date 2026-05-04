
class BookNotFoundException(Exception):
    def __init__(self, book_id: int):
        super().__init__(f"Book with id {book_id} not found.")
