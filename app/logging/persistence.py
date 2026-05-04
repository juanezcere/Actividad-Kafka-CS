from kafka import KafkaConsumer
from json import loads

from app.domain.models.log import LogModel
from app.infrastructure.adapters.repositories.sqlite_log_repository import SQLiteLogRepository

repo = SQLiteLogRepository()


def eternal(function):
    def wrapper(*args, **kwargs):
        while True:
            function(*args, **kwargs)
    return wrapper


class LogPersistenceService:
    def __init__(self, topic: str, server_url: str, group_id: str = 'test-group'):
        self.consumer: KafkaConsumer = KafkaConsumer(
            topic,
            bootstrap_servers=server_url,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=group_id,
            value_deserializer=lambda x: self.save(loads(x.decode('utf-8')))
        )

    def save(self, message: dict) -> None:
        new_log = LogModel(
            id=None,
            level=message['level'],
            message=message['message'],
            timestamp=message['timestamp'],
            topic=message['topic']
        )
        repo.save(new_log)
        print(f"New log message saved: {new_log}")

    @eternal
    def run(self):
        for message in self.consumer:
            print(f"New log received: {message}")
