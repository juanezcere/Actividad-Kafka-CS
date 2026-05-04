from abc import ABC, abstractmethod

from .logger import LogLevel, ConsoleLogger, KafkaLogger

from ..config import KAFKA_LOGS_TOPIC, KAFKA_SERVER_URL, KAFKA_LOG_LEVEL


class ILogging(ABC):
    @abstractmethod
    def debug(self, message: str) -> None:
        pass

    @abstractmethod
    def info(self, message: str) -> None:
        pass

    @abstractmethod
    def warning(self, message: str) -> None:
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        pass

    @abstractmethod
    def critical(self, message: str) -> None:
        pass


class Logging(ILogging):
    def __init__(self, loggers: list = None):
        self.loggers = loggers or []

    def debug(self, message: str) -> None:
        for logger in self.loggers:
            logger.log(LogLevel.DEBUG, message)

    def info(self, message: str) -> None:
        for logger in self.loggers:
            logger.log(LogLevel.INFO, message)

    def warning(self, message: str) -> None:
        for logger in self.loggers:
            logger.log(LogLevel.WARNING, message)

    def error(self, message: str) -> None:
        for logger in self.loggers:
            logger.log(LogLevel.ERROR, message)

    def critical(self, message: str) -> None:
        for logger in self.loggers:
            logger.log(LogLevel.CRITICAL, message)


logging = Logging()


def configure_console_logging(level: LogLevel = LogLevel.NOTSET) -> None:
    logging.loggers += [ConsoleLogger(level), ]


def configure_kafka_logging(topic: str, server_url: str, level: LogLevel = LogLevel.NOTSET) -> None:
    logging.loggers += [KafkaLogger(level, topic, server_url)]
