''' Module for the Art-Payload '''
import base64
from io import BytesIO
from PIL import Image
from payloads.base import BasePayload

class Art(BasePayload):
    '''Art-Payload'''
    def __init__(self, jpg, player, ms, type_iterable, version):
        super().__init__(ms)
        self.jpg = jpg
        self.player = player
        self.ms = ms
        self.type_iterable = type_iterable
        self.version = version

    @classmethod
    def from_json(cls, data):
        '''Creates an instance of the class from a JSON object'''
        payload = data.get('payload', {})
        jpg = payload.get('jpg')
        player = payload.get('player')
        ms = data.get('ms')
        type_iterable = data.get('type')
        version = data.get('version')
        return cls(jpg, player, ms, type_iterable, version)

    def to_dict(self):
        '''Returns a dictionary representation of the object'''
        return {
            'jpg': self.jpg,
            'player': self.player,
            'ms': self.ms,
            'type': self.type_iterable,
            'version': self.version,
        }
    
    def save_player_image(self):
        '''Saves an image using the player's number in the filename'''
        try:
            print("Decoding base64 data...")
            image_data = base64.b64decode(self.jpg)
            print("Opening image...")
            image = Image.open(BytesIO(image_data))
    
            # Create the filename using the player number
            filename = f"{self.player}.jpg"
            output_path = f"data/{filename}"
    
            print(f"Saving image as {output_path}...")
            # Save the image as JPEG
            image.save(output_path, 'JPEG')
            print(f"Image saved successfully as {output_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def __str__(self):
        base_str = super().__str__()
        return (f'{base_str}: '
                f'type:{self.type_iterable}, '
                f'player:{self.player}, '
                f'jpg:{self.jpg[:10]}...')
