from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import Optional, List

from app.models.user import Channel
from app.models.user import Subscription
from app.services.channel_service import ChannelService
from app.core.database import get_session

router = APIRouter()

@router.post("/channel/", response_model=Channel)
def create_channel(channel: Channel, session: Session = Depends(get_session)):
    channel_service = ChannelService(session)
    return channel_service.create_channel(channel)

@router.get("/channel/{channel_id}", response_model=Channel)
def create_channel(channel_id: int, session: Session = Depends(get_session)):
    channel_service = ChannelService(session)
    return channel_service.get(channel_id)

