'''importing the BasePayload class from the base module'''
from .base import BasePayload
'''Module to represent a device'''
class Device (BasePayload):
    '''Device class to represent a device'''
    def __init__(self, active, name, player, ms, type_iterable, version):
        super().__init__(ms)
        self.active = active
        self.name = name
        self.player = player
        self.ms = ms
        self.type_iterable = type_iterable
        self.version = version

    def __repr__(self):
        return (f'Device(active={self.active}, name={self.name}, player={self.player}, '
                f'ms={self.ms}, type={self.type_iterable}, version={self.version})')

    @classmethod
    def from_json(cls, data):
        '''Creates an instance of the class from a JSON object'''
        payload = data.get('payload', {})
        active = payload.get('active')
        name = payload.get('name')
        player = payload.get('player')
        ms = data.get('ms')
        type_iterable = data.get('type')
        version = data.get('version')
        return cls(active, name, player, ms, type_iterable, version)

    def to_dict(self):
        '''Returns a dictionary representation of the object'''
        base_str = super().__str__()
        return {
            'active': self.active,
            'name': self.name,
            'player': self.player,
            'ms': self.ms,
            'type': self.type_iterable,
            'version': self.version
        }
