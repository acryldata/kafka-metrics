from confluent_kafka.admin import AdminClient

# Kafka AdminClient configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
}

# Create AdminClient instance
admin_client = AdminClient(conf)

# Fetch metadata
metadata = admin_client.list_topics(timeout=10)

# List available topics
topics = metadata.topics
print("Available topics:")
for topic in topics:
    print(topic)
