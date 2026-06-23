class MainException:
    def __init__(self, message):
        self.message = message

class NewException(MainException):
    def __init__(self, message):
        super().__init__(message)