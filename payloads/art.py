'''importing the BasePayload class from the base module'''
from .base import BasePayload
class Art(BasePayload):
    '''Art-Payload'''
    def __init__(self, track_jpg, player, ms, type_iterable, version):
        super().__init__(ms)
        self.track_jpg = track_jpg
        self.player = player
        self.ms = ms
        self.type_iterable = type_iterable
        self.version = version

    @classmethod
    def from_json(cls, data):
        '''Creates an instance of the class from a JSON object'''
        payload = data.get('payload', {})
        track_jpg = payload.get('jpg')
        player = payload.get('player')
        ms = data.get('ms')
        type_iterable = data.get('type')
        version = data.get('version')
        return cls(track_jpg, player, ms, type_iterable, version)
    def to_dict(self):
        '''Returns a dictionary representation of the object'''
        return {
            'jpg': self.track_jpg,
            'player': self.player,
            'ms': self.ms,
            'type': self.type_iterable,
            'version': self.version
        }
    def __str__(self):
        base_str = super().__str__()
        return (f'{base_str}, '
            f'type:{self.type_iterable}, '
            f'jpg:{self.track_jpg}, '
            f'player:{self.player}, '
            f'version:{self.version})')
