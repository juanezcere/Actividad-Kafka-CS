from dataclasses import dataclass
from typing import Optional


@dataclass
class BookModel:
    id: Optional[int]
    title: str
    author: str
    description: str
    pages: int
    rating: int
