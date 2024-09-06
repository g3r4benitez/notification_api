from pydantic import BaseModel


class Notification(BaseModel):
    category: str
    message: str
