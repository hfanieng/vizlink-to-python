''' Import the BasePayload class from the base module '''
from .base import BasePayload


class Sys(BasePayload):
    ''' Define the Sys class that inherits from BasePayload '''

    def __init__(self, code, msg, ms, type, version):
        super().__init__(ms)
        self.code = code
        self.msg = msg
        self.ms = ms
        self.type = type
        self.version = version

    @classmethod
    def from_json(cls, data):
        ''' Create a new instance of the Sys class from a JSON object '''
        payload = data.get('payload', {})
        code = payload.get('code')
        msg = payload.get('msg')
        ms = data.get('ms')
        type = data.get('type')
        version = data.get('version')
        return cls(code, msg, ms, type, version)

    def to_dict(self):
        ''' Convert the Sys object to a dictionary'''
        return {
            'code': self.code,
            'msg': self.msg,
            'ms': self.ms,
            'type': self.type,
            'version': self.version
        }

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}, Type:{self.type}, Code:{self.code}, Msg:{self.msg}, Version:{self.version})")
