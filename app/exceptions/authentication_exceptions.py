from fastapi import status
from typing import Iterable
from app.core.error_handler import HTTPCustomException


class ForbiddenException(HTTPCustomException):
    def __init__(self, message: str = "Forbidden", **kwargs):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, msg=message, **kwargs)


class UnauthorizedException(HTTPCustomException):
    def __init__(self, message: str = "Unauthorized", **kwargs):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, msg=message, **kwargs)


class MissingUserMetadataError(HTTPCustomException):
    """Error for missing metadata."""

    def __init__(self, missing_fields: Iterable[str]):
        self.missing_fields = missing_fields

    def args(self):
        return self.missing_fields

    def __str__(self):
        return 'Missing user metadata: {}'.format(
            ', '.join(self.missing_fields)
        )
