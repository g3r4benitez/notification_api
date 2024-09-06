from fastapi import status

from app.core.error_handler import HTTPCustomException


class ConflictExeption(HTTPCustomException):
    DEFAULT_MESSAGE = "Entity id already used"

    def __init__(self, message: str = DEFAULT_MESSAGE, **kwargs):
        super().__init__(status_code=status.HTTP_409_CONFLICT, msg=message, **kwargs)

class UnauthorizedException(HTTPCustomException):
    def __init__(self, message: str = "Unauthorized", **kwargs):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, msg=message, **kwargs)


class TooManyRequestException(HTTPCustomException):
    def __init__(self, message: str = "too many request", **kwargs):
        super().__init__(status_code=status.HTTP_429_TOO_MANY_REQUESTS, msg=message, **kwargs)


class BadRequestException(HTTPCustomException):
    DEFAULT_MESSAGE = "Invalid parameters"

    def __init__(self, message: str = DEFAULT_MESSAGE, **kwargs):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, msg=message, **kwargs)

class InternalServerError(HTTPCustomException):
    DEFAULT_MESSAGE = "Internal Server Error"

    def __init__(self, message: str = DEFAULT_MESSAGE, **kwargs):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, msg=message, **kwargs)
