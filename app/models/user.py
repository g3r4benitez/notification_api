from pydantic import BaseModel, EmailStr
from typing import List


class User(BaseModel):
    name: str
    email: EmailStr
    phone_number: int
    subscribed: List[int]
    channels: str

    class Config:
        orm_mode = True
