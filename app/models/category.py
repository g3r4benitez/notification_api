from pydantic import BaseModel, EmailStr


class Category(BaseModel):
    name: str

    class Config:
        orm_mode = True
