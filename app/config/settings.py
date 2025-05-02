import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings that can be loaded from environment variables
    """
    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "InsightService"
    
    # OpenAI settings
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    # Kafka settings
    KAFKA_BOOTSTRAP_SERVERS: str = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
    KAFKA_TOPIC: str = os.getenv("KAFKA_TOPIC", "insights")
    KAFKA_RETRIES: int = int(os.getenv("KAFKA_RETRIES", "5"))
    KAFKA_RETRY_BACKOFF_MS: int = int(os.getenv("KAFKA_RETRY_BACKOFF_MS", "1000"))
    
    # Logging settings
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()