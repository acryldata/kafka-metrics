import sys
import os

from shared.KafkaConfig import KafkaConfig
from shared.KafkaMonitor import KafkaMonitor
from shared.TimestampChecker import TimestampChecker

import time
from datetime import datetime

def main():
    kafka_brokers = 'localhost:9092'
    schema_registry_url = 'http://localhost:8081'
    group_id = 'my_group_id'
    topic = 'MetadataChangeLog_Versioned_v1'
    time_offset_seconds = 600  # 1 minute threshold

    kafka_config = KafkaConfig(kafka_brokers, schema_registry_url, group_id)
    kafka_monitor = KafkaMonitor(kafka_config, topic)
    timestamp_checker = TimestampChecker(time_offset_seconds)

    while True:
        latest_timestamp = kafka_monitor.get_latest_message_timestamp()
        if latest_timestamp:
            is_stale = timestamp_checker.is_timestamp_stale(latest_timestamp)
            if is_stale:
                print(f"Latest message timestamp {datetime.fromtimestamp(latest_timestamp / 1000.0)} is older than the {time_offset_seconds} second threshold.")
            else:
                print(f"Latest message timestamp {datetime.fromtimestamp(latest_timestamp / 1000.0)} is within the acceptable {time_offset_seconds} second range.")
        else:
            print("No new messages found.")
        
        # Wait before checking again
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()
