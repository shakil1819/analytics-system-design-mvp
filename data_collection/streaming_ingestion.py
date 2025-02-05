from kafka import KafkaProducer, KafkaConsumer
import json

# Kafka configuration
KAFKA_TOPIC = 'data_topic'
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'

# Producer for streaming ingestion
class KafkaStreamProducer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send_data(self, data):
        self.producer.send(KAFKA_TOPIC, data)
        self.producer.flush()

# Consumer for streaming ingestion
class KafkaStreamConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )

    def consume_data(self):
        for message in self.consumer:
            print(f"Received data: {message.value}")
