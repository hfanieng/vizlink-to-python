''' This module contains the Structure class, which is a subclass of BasePayload.'''
from .base import BasePayload
class Structure(BasePayload):
    ''' This class represents a Structure payload. It contains the following attributes:'''
    def __init__(self, bank, mood, phrases, player, ms, type_iterable, version):
        super().__init__(ms)
        self.bank = bank
        self.mood = mood
        self.phrases = phrases  # List von Dictionaries
        self.player = player
        self.type_iterable = type_iterable
        self.version = version

    @classmethod
    def from_json(cls, data):
        ''' This method creates a Structure object from a JSON object.'''
        payload = data.get('payload', {})
        bank = payload.get('bank')
        mood = payload.get('mood')
        phrases = payload.get('phrases', [])
        player = payload.get('player')
        ms = data.get('ms')
        type_iterable = data.get('type')
        version = data.get('version')
        return cls(bank, mood, phrases, player, ms, type_iterable, version)

    def to_dict(self):
        ''' This method converts a Structure object to a dictionary.'''
        return {
            'bank': self.bank,
            'mood': self.mood,
            'phrases': self.phrases,
            'player': self.player,
            'ms': self.ms,
            'type': self.type_iterable,
            'version': self.version
        }

    def __str__(self):
        base_str = super().__str__()
        return (f'{base_str}, '
                f'Type:{self.type_iterable}, '
                f'Bank:{self.bank}, '
                f'Mood:{self.mood}, '
                f'Phrases:{self.phrases}, '
                f'Player:{self.player}, '
                f'Version:{self.version})')
