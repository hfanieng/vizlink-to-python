class Device:
    def __init__(self, active, name, player, ms, type, version):
        self.active = active
        self.name = name
        self.player = player
        self.ms = ms
        self.type = type
        self.version = version

    def __repr__(self):
        return (f'Device(active={self.active}, name={self.name}, player={self.player}, '
                f'ms={self.ms}, type={self.type}, version={self.version})')

    @classmethod
    def from_json(cls, data):
        payload = data.get('payload', {})
        active = payload.get('active')
        name = payload.get('name')
        player = payload.get('player')
        ms = data.get('ms')
        type = data.get('type')
        version = data.get('version')
        return cls(active, name, player, ms, type, version)

    def to_dict(self):
        return {
            'active': self.active,
            'name': self.name,
            'player': self.player,
            'ms': self.ms,
            'type': self.type,
            'version': self.version
        }
