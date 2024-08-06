class Error:
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __repr__(self):
        return f'Error(code={self.code}, message="{self.message}")'
