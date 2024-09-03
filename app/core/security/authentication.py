from fastapi import Security
from fastapi.security.api_key import APIKeyHeader
from functools import wraps

from app.repositories import user_repository
from app.exceptions.general_exeptions import UnauthorizedException
from app.core.config import API_KEY_NAME

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def validate_api_key(api_key_header: str = Security(api_key_header)):

    if not api_key_header or not user_repository.get_user_using_apikey(api_key_header):
        raise UnauthorizedException("Apikey is not valid")



def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        apikey = kwargs.get('apikey')
        if not user_repository.get_user_using_apikey(apikey):
            raise UnauthorizedException("Apikey is not valid")
        return func(*args, **kwargs)
    return wrapper


