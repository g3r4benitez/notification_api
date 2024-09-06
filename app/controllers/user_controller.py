from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import Optional, List

from app.models.user import User
from app.models.user import Subscription
from app.services.user_service import UserService
from app.core.database import get_session

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    user_service = UserService(session)
    return user_service.create_user(user)

@router.post("/users/{user_id}/subscriptions/{subscription_id}/")
def add_subscription_to_user(user_id: int, subscription_id: int, session: Session = Depends(get_session)):
    user_service = UserService(session)
    link = user_service.add_subscription_to_user(user_id, subscription_id)
    if not link:
        raise HTTPException(status_code=404, detail="User or Subscription not found")
    return {"message": "Subscription added to user"}

@router.get("/users/{user_id}/subscriptions/", response_model=List[Subscription])
def get_user_subscriptions(user_id: int, session: Session = Depends(get_session)):
    user_service = UserService(session)
    return user_service.get_user_subscriptions(user_id)

@router.get("/subscriptions/{subscription_id}/users/", response_model=List[User])
def get_users_of_subscription(subscription_id: int, session: Session = Depends(get_session)):
    user_service = UserService(session)
    return user_service.get_users_of_subscription(subscription_id)
