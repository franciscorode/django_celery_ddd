class UserAlreadyExist(Exception):
    pass


class InvalidEmailContentData(Exception):
    def __init__(self, message: str):
        super().__init__(message)
