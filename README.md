# Kafka Metrics Collector

This project is a Kafka metrics collector used to monitor the freshness of messages in a Kafka topic. It is designed to work with Acryl DataHub to ensure timely processing of metadata change logs.

## Overview

The Kafka Metrics Collector is composed of three main components:

1. **KafkaConfig**: Handles the configuration for Kafka and the Schema Registry.
2. **KafkaMonitor**: Monitors a specified Kafka topic and retrieves the timestamp of the most recent message.
3. **TimestampChecker**: Checks if the timestamp of the most recent message is older than a specified threshold.

## Project Structure

```
project/
│
├── shared/
│   ├── KafkaConfig.py
│   ├── KafkaMonitor.py
│   └── TimestampChecker.py
│
└── collect-metrics.py
```

### Components

- **KafkaConfig**: Manages Kafka and Schema Registry configuration.
- **KafkaMonitor**: Subscribes to a Kafka topic and fetches the latest message's timestamp.
- **TimestampChecker**: Compares the message timestamp with a specified freshness threshold.

## Requirements

- Python 3.7+
- `confluent_kafka`
- `fastavro`
- `requests`

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd project
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the required packages:

```bash
pip install confluent_kafka fastavro requests
```

## Configuration

Modify the `collect-metrics.py` script to set your Kafka broker, Schema Registry URL, and the desired topic and group ID:

```python
kafka_brokers = 'localhost:9092'
schema_registry_url = 'http://localhost:8081'
group_id = 'my_group_id'
topic = 'MetadataChangeLog_Versioned_v1'
time_offset_seconds = 60  # 1 minute threshold
```

## Usage

Run the `collect-metrics.py` script to start monitoring the Kafka topic and collecting metrics:

```bash
python collect-metrics.py
```

### Expected Output

The script will periodically print whether the latest message in the Kafka topic is within the acceptable range or if it is stale based on the specified threshold.

```plaintext
Latest message timestamp 2023-05-21 10:00:00 is within the acceptable range.
No new messages found.
Latest message timestamp 2023-05-21 09:55:00 is older than the threshold.
```

The output will help you determine if the messages in your Kafka topic are being processed in a timely manner, ensuring the freshness of your data.

### Slack Thread Integration

This project was created to ensure that the metadata change logs in Acryl DataHub are processed promptly. By regularly monitoring the timestamp of the most recent message in a Kafka topic, you can determine if the data is fresh or if there are delays in processing.

The Kafka Metrics Collector script continuously checks the most recent message timestamp and compares it against a specified threshold. If the message timestamp is older than the threshold, it indicates that the data is stale and may require attention.

By running this script, you can automate the monitoring of your Kafka topics and ensure that your data processing pipeline remains efficient and up-to-date.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- This project uses [Apache Kafka](https://kafka.apache.org/) and [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/index.html).
- [Acryl DataHub](https://datahubproject.io/) for inspiring the need for timely metadata processing.

Feel free to contribute to the project by opening issues or submitting pull requests. Happy monitoring!