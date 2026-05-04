from dataclasses import dataclass
from typing import Optional


@dataclass
class BookModel:
    id: Optional[int]
    title: str
    author: str
    pages: int
    description: str
    rating: int
