from confluent_kafka import DeserializingConsumer, KafkaError, KafkaException
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka.serialization import StringDeserializer

# Kafka Consumer configuration
kafka_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_group_id',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False,
}

# Schema Registry configuration
schema_registry_url = 'http://localhost:8081'
schema_registry_conf = {'url': schema_registry_url}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

# Avro Deserializer
avro_deserializer = AvroDeserializer(schema_registry_client)
string_deserializer = StringDeserializer('utf_8')

# Create DeserializingConsumer instance
consumer_conf = {
    **kafka_conf,
    'key.deserializer': string_deserializer,
    'value.deserializer': avro_deserializer
}
consumer = DeserializingConsumer(consumer_conf)

# Subscribe to topic
topic = 'MetadataChangeLog_Versioned_v1'
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('%% %s [%d] reached end at offset %d\n' %
                      (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            # Decode Avro message
            message_value = msg.value()
            # Get the timestamp
            timestamp_type, timestamp = msg.timestamp()
            timestamp_type_str = "CreateTime" if timestamp_type == 0 else "LogAppendTime"
            print(f"Received message: {message_value} at timestamp: {timestamp} ({timestamp_type_str})")

except KeyboardInterrupt:
    pass
finally:
    # Close down consumer to commit final offsets.
    consumer.close()
