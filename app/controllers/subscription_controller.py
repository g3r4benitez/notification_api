from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.user import Subscription
from app.services.subscription_service import SubscriptionService
from app.core.database import get_session

router = APIRouter()

@router.post("", response_model=Subscription)
def create_subscription(subscription: Subscription, session: Session = Depends(get_session)):
    subscription_service = SubscriptionService(session)
    return subscription_service.create_subscription(subscription)

@router.get("/{subscription_id}", response_model=Subscription)
def create_channel(subscription_id: int, session: Session = Depends(get_session)):
    subscription_service = SubscriptionService(session)
    return subscription_service.get(subscription_id)

