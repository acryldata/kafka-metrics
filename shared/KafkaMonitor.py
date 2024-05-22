from confluent_kafka import DeserializingConsumer, KafkaError, KafkaException

class KafkaMonitor:
    def __init__(self, kafka_config, topic):
        self.consumer = DeserializingConsumer(kafka_config.get_consumer_config())
        self.topic = topic
        self.consumer.subscribe([self.topic])

    def get_latest_message_timestamp(self):
        try:
            msg = self.consumer.poll(timeout=1.0)
            if msg is None:
                return None
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f'%% {msg.topic()} [{msg.partition()}] reached end at offset {msg.offset()}')
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                _, timestamp = msg.timestamp()
                return timestamp
        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()
        return None
