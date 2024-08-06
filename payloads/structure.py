from .base import BasePayload


class Structure(BasePayload):
    def __init__(self, bank, mood, phrases, player, ms, type, version):
        super().__init__(ms)
        self.bank = bank
        self.mood = mood
        self.phrases = phrases  # List von Dictionaries
        self.player = player
        self.type = type
        self.version = version

    @classmethod
    def from_json(cls, data):
        payload = data.get('payload', {})
        bank = payload.get('bank')
        mood = payload.get('mood')
        phrases = payload.get('phrases', [])
        player = payload.get('player')
        ms = data.get('ms')
        type = data.get('type')
        version = data.get('version')
        return cls(bank, mood, phrases, player, ms, type, version)

    def to_dict(self):
        return {
            'bank': self.bank,
            'mood': self.mood,
            'phrases': self.phrases,
            'player': self.player,
            'ms': self.ms,
            'type': self.type,
            'version': self.version
        }

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}, Type:{self.type}, Bank:{self.bank}, Mood:{self.mood}, Phrases:{self.phrases}, "
                f"Player:{self.player}, Version:{self.version})")
