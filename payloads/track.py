from .base import BasePayload


class Track (BasePayload):
    def __init__(self, album, artist, cues, duration, player, source, tempo, title, year, ms, type, version):
        super().__init__(ms)
        self.album = album
        self.artist = artist
        self.cues = cues
        self.duration = duration
        self.player = player
        # Hier kann das Source-Objekt als Dictionary oder in einer eigenen Klasse verwendet werden
        self.source = source
        self.tempo = tempo
        self.title = title
        self.year = year
        self.ms = ms
        self.type = type
        self.version = version

    @classmethod
    def from_json(cls, data):
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
        type = data.get('type')
        version = data.get('version')
        return cls(album, artist, cues, duration, player, source, tempo, title, year, ms, type, version)

    def to_dict(self):
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
            'type': self.type,
            'version': self.version
        }

    def __str__(self):
        base_str = super().__str__()
        return (f'{base_str}, Type:{self.type}, Title:{self.title}, Artist:{self.artist}, Album: {self.album},  cues={self.cues}, '
                f'duration={self.duration}, player={
                    self.player}, source={self.source}, '
                f'tempo={self.tempo}, year={self.year},version={self.version})')
