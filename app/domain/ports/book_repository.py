from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.models.book import BookModel


class BookRepository(ABC):
    @abstractmethod
    def save(self, book: BookModel) -> BookModel:
        pass

    @abstractmethod
    def find_all(self) -> List[BookModel]:
        pass

    @abstractmethod
    def find_by_id(self, book_id: int) -> Optional[BookModel]:
        pass

    @abstractmethod
    def delete(self, book_id: int) -> bool:
        pass
