from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.models.user import Channel
from app.services.channel_service import ChannelService
from app.core.database import get_session
from app.core.logger import logger

router = APIRouter()

@router.post("", response_model=Channel)
def create_channel(channel: Channel, session: Session = Depends(get_session)):
    channel_service = ChannelService(session)
    return channel_service.create_channel(channel)

@router.get("/{channel_id}", response_model=Channel)
def get_channel(channel_id: int, session: Session = Depends(get_session)):
    channel_service = ChannelService(session)
    return channel_service.get(channel_id)

@router.get("")
def get_channels(session: Session = Depends(get_session)):
    channel_service = ChannelService(session)
    return channel_service.get_all()
