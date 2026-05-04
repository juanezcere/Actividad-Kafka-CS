from typing import List

from app.domain.ports.log_repository import LogRepository
from app.domain.models.log import LogModel


class GetAllLogs:
    def __init__(self, repository: LogRepository):
        self.repository = repository

    def execute(self) -> List[LogModel]:
        return self.repository.find_all()
