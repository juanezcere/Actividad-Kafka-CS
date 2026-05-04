from fastapi import FastAPI
import uvicorn
import threading

import app.config as config

from app.logging.logging import configure_console_logging, configure_kafka_logging, LogLevel
from app.logging.persistence import LogPersistenceService
from app.infrastructure.adapters.api.book_controller import router as book_router
from app.infrastructure.adapters.api.log_controller import router as log_router
from app.logging.logging import logging


def configure_logging():
    topic = config.KAFKA_LOGS_TOPIC or "AppTestingLogs"
    server_url = config.KAFKA_SERVER_URL or "192.168.1.24:9092"
    configure_console_logging(LogLevel.INFO)
    configure_kafka_logging(topic, server_url, LogLevel.DEBUG)
    logging.debug("Logging configured successfully.")
    log_service = LogPersistenceService(topic, server_url)
    thread = threading.Thread(target=log_service.run)
    logging.info("Starting log persistence service...")
    thread.start()


def configure_app():
    logging.info("Configuring app...")
    title: str = config.APP_TITLE or "Testing App"
    description: str = config.APP_DESCRIPTION or "Testing App description."
    version: str = config.APP_VERSION or "1.0.0"
    app = FastAPI(title=title, description=description, version=version)
    app.include_router(log_router)
    app.include_router(book_router)
    logging.info("App configured successfully.")
    return app


def configure_server(app: FastAPI):
    host = config.APP_HOST or "0.0.0.0"
    port = config.APP_PORT or 8000
    logging.info(f"Starting server on {host}:{port}...")
    uvicorn.run(app, host=host, port=int(port))


def main():
    configure_logging()
    app = configure_app()
    configure_server(app)


if __name__ == "__main__":
    main()
