from abc import ABC, abstractmethod
from typing import List

from app.domain.models.log import LogModel


class LogRepository(ABC):
    @abstractmethod
    def save(self, log: LogModel) -> LogModel:
        pass

    @abstractmethod
    def find_all(self) -> List[LogModel]:
        pass
