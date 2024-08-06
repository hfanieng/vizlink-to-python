import datetime


class BasePayload:
    def __init__(self, ms):
        self.ms = ms

    def convert_ms_to_datetime(self):
        seconds = self.ms / 1000.0
        date_time = datetime.datetime.fromtimestamp(seconds)
        return date_time.strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return self.convert_ms_to_datetime()
