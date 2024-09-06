from sqlmodel import Session, select
from app.models.user import Subscription
from app.core.database import engine


class SubscriptionService:
    def __init__(self, session: Session):
        self.session = session

    def create_subscription(self, subscription: Subscription) -> Subscription:
        self.session.add(subscription)
        self.session.commit()
        self.session.refresh(subscription)
        return subscription

    def get(self, _id: int):
        obj = self.session.get(Subscription, _id)
        return obj

    def get_by_name(self, name: str):
        statement = select(Subscription).where(Subscription.name == name)
        results = self.session.exec(statement)
        return results.first()


session = Session(engine)
subscription_service = SubscriptionService(session)



