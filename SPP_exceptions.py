class AbstractException(Exception):
    """Exception to be used for abstract classes."""
    def __str__(self):
        return "Please implement all the methods."