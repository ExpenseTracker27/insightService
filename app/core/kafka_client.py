import json
import logging
from typing import Dict, Any

from kafka import KafkaProducer
from kafka.errors import KafkaError

from app.config.settings import settings

logger = logging.getLogger(__name__)


class KafkaClient:
    """
    Kafka client for sending messages to topics
    """
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS.split(","),
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            retries=settings.KAFKA_RETRIES,
            retry_backoff_ms=settings.KAFKA_RETRY_BACKOFF_MS,
            acks="all"
        )
        self.default_topic = settings.KAFKA_TOPIC

    def send_message(self, data: Dict[str, Any], topic: str = None) -> bool:
        """
        Send a message to Kafka topic
        
        Args:
            data: Dictionary of data to send
            topic: Topic to send to (uses default from settings if None)
            
        Returns:
            bool: True if the message was sent successfully
        """
        topic = topic or self.default_topic
        try:
            future = self.producer.send(topic, data)
            record_metadata = future.get(timeout=10)
            logger.info(
                f"Message sent to topic {topic} at partition {record_metadata.partition} "
                f"with offset {record_metadata.offset}"
            )
            return True
        except KafkaError as e:
            logger.error(f"Failed to send message to Kafka: {str(e)}")
            return False


# Create a singleton instance
kafka_client = KafkaClient()