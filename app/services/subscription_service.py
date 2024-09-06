from sqlmodel import Session, select
from app.models.user import Subscription
from app.core.database import engine
from app.exceptions.general_exeptions import BadRequestException
from app.core.logger import logger


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
        subscription = results.first()
        if subscription:
            return subscription
        else:
            logger.error(f"Subscription '{name}' doesn't exist")
            raise BadRequestException(message=f"Subscription '{name}' doesn't exists")


session = Session(engine)
subscription_service = SubscriptionService(session)



