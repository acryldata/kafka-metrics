from datetime import datetime, timedelta

class TimestampChecker:
    def __init__(self, time_offset_seconds):
        self.time_offset = timedelta(seconds=time_offset_seconds)

    def is_timestamp_stale(self, message_timestamp, evaluation_time=None):
        if evaluation_time is None:
            evaluation_time = datetime.now()
        message_time = datetime.fromtimestamp(message_timestamp / 1000.0)
        threshold_time = evaluation_time - self.time_offset
        return message_time < threshold_time
