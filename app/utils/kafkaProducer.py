from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    retries=5,
    retry_backoff_ms=1000,
    acks='all'
)

KAFKA_TOPIC = "insights"

def send_to_queue(topic, data):
    try:
        future = producer.send(topic, data)
        record_metadata = future.get(timeout=10)
        print(f"Message sent successfully to topic {topic} at partition {record_metadata.partition} with offset {record_metadata.offset}")
    except KafkaError as e:
        print(f"Failed to send message to Kafka: {str(e)}")

