from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from typing import List

from app.models.orm import Base
from app.models.orm.category import Category


user_category_table = Table(
    "user_category",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("category_id", ForeignKey("category.id")),
)



class User(Base):
    __tablename__: str = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    phone_number = Column(Integer)
    subscribed: Mapped[List[Category]] = relationship(secondary=user_category_table)
    channels = Column(String(255))

    def __init__(self, name, email, phone_number, subscribed, channels):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.subscribed = subscribed
        self.channels = channels

    def __str__(self):
        return f"userId: {self.id}, name: {self.name}, " \
               f"email: {self.email}, phone_number: {self.phone_number}, " \
               f"subscribed: {self.subscribed}, channels: {self.channels}"


