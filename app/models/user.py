from pydantic import EmailStr
from typing import List, Optional
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: EmailStr
    phone_number: int
    subscribed: str
    channels: str

