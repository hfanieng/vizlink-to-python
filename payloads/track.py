'''importing the BasePayload class from the base module'''
from .base import BasePayload
class Track (BasePayload):
    '''Track-Payload'''
    def __init__(self, album, artist, cues, duration, player, source,
                tempo, title, year, ms, type_iterable, version):
        super().__init__(ms)
        self.album = album
        self.artist = artist
        self.cues = cues
        self.duration = duration
        self.player = player
        self.source = source
        self.tempo = tempo
        self.title = title
        self.year = year
        self.ms = ms
        self.type_iterable = type_iterable
        self.version = version

    @classmethod
    def from_json(cls, data):
        '''Creates an instance of the class from a JSON object'''
        payload = data.get('payload', {})
        album = payload.get('album')
        artist = payload.get('artist')
        cues = payload.get('cues', [])
        duration = payload.get('duration')
        player = payload.get('player')
        source = payload.get('source', {})
        tempo = payload.get('tempo')
        title = payload.get('title')
        year = payload.get('year')
        ms = data.get('ms')
        type_iterable = data.get('type')
        version = data.get('version')
        return cls(album, artist, cues, duration, player, source, tempo,
        title, year, ms, type_iterable, version)

    def to_dict(self):
        '''Returns a dictionary representation of the object'''
        return {
            'album': self.album,
            'artist': self.artist,
            'cues': self.cues,
            'duration': self.duration,
            'player': self.player,
            'source': self.source,
            'tempo': self.tempo,
            'title': self.title,
            'year': self.year,
            'ms': self.ms,
            'type': self.type_iterable,
            'version': self.version
        }

    def __str__(self):
        base_str = super().__str__()
        return (f'{base_str}, '
                f'type:{self.type_iterable}, '
                f'title:{self.title}, '
                f'artist:{self.artist}, '
                f'album: {self.album}, '
                f'cues={self.cues}, '
                f'duration={self.duration}, '
                f'player={self.player}, '
                f'source={self.source}, '
                f'tempo={self.tempo}, '
                f'year={self.year}, '
                f'version={self.version})')
