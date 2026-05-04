from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
from kafka import KafkaProducer
from json import dumps


class LogLevel(Enum):
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


class ILogger(ABC):
    @abstractmethod
    def format(self, level: LogLevel, message: str) -> str:
        pass

    @abstractmethod
    def log(self, level: LogLevel, message: str) -> None:
        pass


class ConsoleLogger(ILogger):
    def __init__(self, level: LogLevel) -> None:
        self.level = level

    def format(self, level: LogLevel, message: str) -> str:
        return f"{level.name}: {message}"

    def log(self, level: LogLevel, message: str) -> None:
        if level.value < self.level.value:
            return
        print(self.format(level, message))


class KafkaLogger(ILogger):
    def __init__(self, level: LogLevel, topic: str, url: str) -> None:
        self.level = level
        self.topic: str = topic
        self.producer = KafkaProducer(bootstrap_servers=url)

    def format(self, level: LogLevel, message: str) -> str:
        return dumps({
            "timestamp": str(datetime.now()),
            "topic": self.topic,
            "level": level.name,
            "message": message,
        })

    def log(self, level: LogLevel, message: str) -> None:
        if level.value < self.level.value:
            return
        msg = self.format(level, message)
        self.producer.send(self.topic, msg.encode('utf-8'))
        self.producer.flush()
