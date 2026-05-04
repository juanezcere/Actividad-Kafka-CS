from dataclasses import dataclass
from typing import Optional


@dataclass
class LogModel:
    id: Optional[int]
    timestamp: str
    topic: str
    level: str
    message: str
