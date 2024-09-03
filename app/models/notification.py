from pydantic import BaseModel
from datetime import datetime


class Notification(BaseModel):
    channel: str
    message: str
    date_creation: datetime

    class Config:
        orm_mode = True
