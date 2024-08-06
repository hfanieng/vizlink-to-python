''' This module is responsible for creating payloads based on the payload type. 
Das Modul ist dafür verantwortlich, Payloads auf der Grundlage des Payload-Typs zu erstellen. '''

import json

from payloads.device import Device
from payloads.error import Error
from payloads.sys import Sys
from payloads.track import Track
from .payloads.beat import Beat


class PayloadFactory:
    ''' The PayloadFactory class provides a static method create_payload 
    that takes a payload type and a JSON string as input.
    Die Klasse PayloadFactory bietet eine statische Methode create_payload, 
    die einen Payload-Typ und einen JSON-String als Eingabe erhält.'''
    @staticmethod
    def create_payload(payload_type, json_str):
        ''' The create_payload method parses the JSON string and creates 
        the corresponding payload object.'''
        data = json.loads(json_str)
        if payload_type == 'beat':
            return Beat(**data['beat'])
        elif payload_type == 'device':
            return Device(**data['device'])
        elif payload_type == 'error':
            return Error(**data['error'])
        elif payload_type == 'sys':
            return Sys(**data['sys'])
        elif payload_type == 'track':
            return Track(**data['track'])
        else:
            raise ValueError(f'Unknown payload type: {payload_type}')
