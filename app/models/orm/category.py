from sqlalchemy import Column, Integer, String
from app.models.orm import Base


class Category(Base):
    __tablename__: str = "category"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Category:  {self.name}"


