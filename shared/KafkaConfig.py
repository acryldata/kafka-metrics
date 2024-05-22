from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka.serialization import StringDeserializer

class KafkaConfig:
    def __init__(self, kafka_brokers, schema_registry_url, group_id):
        self.kafka_brokers = kafka_brokers
        self.schema_registry_url = schema_registry_url
        self.group_id = group_id
        self.schema_registry_client = SchemaRegistryClient({"url": self.schema_registry_url})
        self.string_deserializer = StringDeserializer('utf_8')
        self.avro_deserializer = AvroDeserializer(self.schema_registry_client)

    def get_consumer_config(self):
        return {
            'bootstrap.servers': self.kafka_brokers,
            'group.id': self.group_id,
            'auto.offset.reset': 'earliest',
            'enable.auto.commit': False,
            'key.deserializer': self.string_deserializer,
            'value.deserializer': self.avro_deserializer
        }

