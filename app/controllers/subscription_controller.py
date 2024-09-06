from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.user import Subscription
from app.services.subscription_service import SubscriptionService
from app.core.database import get_session

router = APIRouter()

@router.post("/subscription/", response_model=Subscription)
def create_subscription(subscription: Subscription, session: Session = Depends(get_session)):
    subscription_service = SubscriptionService(session)
    return subscription_service.create_subscription(subscription)

@router.get("/subscription/{channel_id}", response_model=Subscription)
def create_channel(channel_id: int, session: Session = Depends(get_session)):
    subscription_service = SubscriptionService(session)
    return subscription_service.get(channel_id)

