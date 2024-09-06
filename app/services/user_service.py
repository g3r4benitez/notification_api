from typing import List
from sqlmodel import Session
from app.models.user import User, Subscription, UserSubscriptionLink, Channel, UserChannelLink
from app.core.database import get_session
from app.core.database import engine


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: User) -> User:
        if user.id == 0:
            user.id = None

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def add_subscription_to_user(self, user_id: int, subscription_id: int):
        user = self.session.get(User, user_id)
        subscription = self.session.get(Subscription, subscription_id)
        if user and subscription:
            link = UserSubscriptionLink(user_id=user.id, subscription_id=subscription.id)
            self.session.add(link)
            self.session.commit()
            return link
        return None

    def add_channels_to_user(self, user_id: int, channel_id: int):
        user = self.session.get(User, user_id)
        channel = self.session.get(Channel, channel_id)
        if user and channel:
            link = UserChannelLink(user_id=user.id, channel_id=channel.id)
            self.session.add(link)
            self.session.commit()
            return link
        return None

    def get_user_subscriptions(self, user_id: int) -> List[Subscription]:
        user = self.session.get(User, user_id)
        if user:
            return user.subscriptions
        return []

    def get_users_of_subscription(self, subscription_id: int) -> List[User]:
        subscription = self.session.get(Subscription, subscription_id)
        if subscription:
            return subscription.users
        return []

    def get_user_channels(self, user_id: int) -> List[Channel]:
        user = self.session.get(User, user_id)
        if user:
            return user.channels
        return []



session = Session(engine)
user_service = UserService(session)