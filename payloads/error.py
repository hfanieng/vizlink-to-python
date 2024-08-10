''' module for error payload '''
class Error:
    """
    A class to represent an error.

    Attributes:
    ----------
    code : int
        The error code.
    message : str
        The error message.
    """

    def __init__(self, code, message):
        """
        Initializes a new instance of the Error class.

        Parameters:
        -----------
        code : int
            The error code.
        message : str
            The error message.
        """
        self.code = code
        self.message = message

    def __repr__(self):
        """
        Returns a string representation of the error.

        Returns:
        --------
        str
            A string representation of the error.
        """
        return f'Error(code={self.code}, message="{self.message}")'
