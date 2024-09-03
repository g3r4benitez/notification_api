from pydantic import BaseModel, EmailStr
from typing import List


class User(BaseModel):
    ID: int
    name: str
    email: EmailStr
    phone_number: int
    subscribed: List[str]
    channels: List[str]


