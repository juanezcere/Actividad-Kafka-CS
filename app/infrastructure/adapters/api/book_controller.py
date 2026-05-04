from fastapi import APIRouter, HTTPException, status
from typing import List

from app.infrastructure.adapters.repositories.sqlite_book_repository import SQLiteBookRepository
from app.application.use_cases.create_book import CreateBook
from app.application.use_cases.get_all_books import GetAllBooks
from app.application.use_cases.get_book import GetBook
from app.application.use_cases.delete_book import DeleteBook
from app.application.use_cases.update_book import UpdateBook
from app.domain.models.book import BookModel

router = APIRouter(prefix="/books", tags=["Books"])
repo = SQLiteBookRepository()


@router.post("/", response_model=BookModel, status_code=status.HTTP_201_CREATED)
async def create_book(title: str, author: str, pages: int, description: str, rating: int):
    use_case = CreateBook(repo)
    return use_case.execute(title, author, pages, description, rating)


@router.get("/", response_model=List[BookModel])
async def get_all_books():
    use_case = GetAllBooks(repo)
    return use_case.execute()


@router.get("/{book_id}", response_model=BookModel)
async def get_book(book_id: int):
    use_case = GetBook(repo)
    book = use_case.execute(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=BookModel)
async def update_book(book_id: int, title: str, author: str, pages: int, description: str, rating: int):
    use_case = UpdateBook(repo)
    try:
        return use_case.execute(book_id, title, author, pages, description, rating)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    use_case = DeleteBook(repo)
    success = use_case.execute(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Can't delete the book")
    return None
