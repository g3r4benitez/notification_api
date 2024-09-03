from fastapi import status

from app.core.error_handler import HTTPCustomException


class NotFound(HTTPCustomException):
    DEFAULT_MESSAGE = "Export Not Found"

    def __init__(self, message: str = DEFAULT_MESSAGE, **kwargs):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, msg=message, **kwargs)