from typing import List

from app.domain.ports.log_repository import LogRepository
from app.domain.models.log import LogModel
from app.logging.logging import logging


class GetAllLogs:
    def __init__(self, repository: LogRepository):
        self.repository = repository

    def execute(self) -> List[LogModel]:
        logging.debug("Getting all logs from GetAllLogs use case...")
        return self.repository.find_all()
