from pydantic import BaseModel
from datetime import datetime


class Notification(BaseModel):
    category: str
    message: str
