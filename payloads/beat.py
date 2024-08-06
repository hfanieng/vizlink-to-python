''' Import the BasePayload class from the base module '''
from .base import BasePayload


class Beat (BasePayload):
    ''' Define the Beat class that inherits from BasePayload '''

    def __init__(self, beat, master, onair, ms, type, version):
        super().__init__(ms)
        self.beat = beat
        self.master = master
        self.onair = onair
        self.type = type
        self.version = version

    @classmethod
    def from_json(cls, data):
        ''' Create a new instance of the Beat class from a JSON object '''
        payload = data.get('payload', {})
        beat = payload.get('beat')
        master = payload.get('master')
        onair = payload.get('onair')
        ms = data.get('ms')
        type = data.get('type')
        version = data.get('version')
        return cls(beat, master, onair, ms, type, version)

    def to_dict(self):
        ''' Convert the Beat object to a dictionary'''
        return {
            'beat': self.beat,
            'master': self.master,
            'onair': self.onair,
            'ms': self.ms,
            'type': self.type,
            'version': self.version
        }

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}, Type:{self.type}, Beat:{self.beat}, Master:{self.master}, Onair:{self.onair}, "
                f" Version:{self.version})")
