from typing import Generator

from app.core.kafka_client import kafka_client
from app.core.llm_service import LLMService
from app.core.message_analyzer import MessageAnalyzer


def get_message_analyzer() -> Generator[MessageAnalyzer, None, None]:
    """Dependency for message analyzer service"""
    analyzer = MessageAnalyzer()
    yield analyzer


def get_llm_service() -> Generator[LLMService, None, None]:
    """Dependency for LLM service"""
    service = LLMService()
    yield service


def get_kafka_client() -> Generator[kafka_client.__class__, None, None]:
    """Dependency for Kafka client"""
    yield kafka_client