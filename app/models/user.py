from pydantic import EmailStr
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship


class UserSubscriptionLink(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, foreign_key="user.id", primary_key=True)
    subscription_id: Optional[int] = Field(default=None, foreign_key="subscription.id", primary_key=True)


class UserChannelLink(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, foreign_key="user.id", primary_key=True)
    channel_id: Optional[int] = Field(default=None, foreign_key="channel.id", primary_key=True)


class Subscription(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    users: List["User"] = Relationship(back_populates="subscriptions", link_model=UserSubscriptionLink)

class Channel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    users: List["User"] = Relationship(back_populates="channels", link_model=UserChannelLink)

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: EmailStr
    phone_number: int
    subscriptions: List["Subscription"] = Relationship(back_populates="users", link_model=UserSubscriptionLink)
    channels: List["Channel"] = Relationship(back_populates="users", link_model=UserChannelLink)