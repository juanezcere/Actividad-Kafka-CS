from fastapi import APIRouter, HTTPException, status
from typing import List

from app.infrastructure.adapters.repositories.sqlite_log_repository import SQLiteLogRepository
from app.application.use_cases.get_all_logs import GetAllLogs
from app.domain.models.log import LogModel

router = APIRouter(prefix="/logs", tags=["Logs"])
repo = SQLiteLogRepository()


@router.get("/", response_model=List[LogModel])
async def get_all_books():
    use_case = GetAllLogs(repo)
    return use_case.execute()
