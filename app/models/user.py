from pydantic import BaseModel, EmailStr
from typing import List


class User(BaseModel):
    ID: int
    name: str
    email: EmailStr
    phone_number: int
    subscribed: List[str]
    channels: List[str]

    def __dict__(self):
        return {
            "ID": self.ID,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number
        }


