from kafka import KafkaConsumer
from json import loads


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
        print(f"Persisting log: {message}.")

    @eternal
    def run(self):
        for message in self.consumer:
            print(message)
