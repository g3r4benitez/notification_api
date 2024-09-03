from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.models.orm import Base


class Notification(Base):
    __tablename__: str = "notification"

    id = Column(Integer, primary_key=True, index=True)
    channel = Column(String(255))
    message = Column(String(255))
    date_creation = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, channel, message, date_creation):
        self.channel = channel
        self.message = message
        self.date_creation = date_creation

    def __str__(self):
        return f"Sending:  {self.message} at {self.date_creation}"


