import app.config as config

from app.logging.logging import configure_console_logging, configure_kafka_logging, LogLevel
from app.services.log_persistence import LogPersistenceService


def main():
    topic = config.KAFKA_LOGS_TOPIC or "AppTestingLogs"
    server_url = config.KAFKA_SERVER_URL or "192.168.1.24:9092"
    configure_console_logging(LogLevel.INFO)
    configure_kafka_logging(topic, server_url, LogLevel.DEBUG)
    log_service = LogPersistenceService(topic, server_url)
    log_service.run()


if __name__ == "__main__":
    main()
