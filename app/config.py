import os
from dotenv import load_dotenv

load_dotenv()

KAFKA_LOGS_TOPIC = os.getenv("KAFKA_LOGS_TOPIC")
KAFKA_SERVER_URL = os.getenv("KAFKA_SERVER_URL")
KAFKA_LOG_LEVEL = os.getenv("KAFKA_LOG_LEVEL")
CONSOLE_LOG_LEVEL = os.getenv("CONSOLE_LOG_LEVEL")
