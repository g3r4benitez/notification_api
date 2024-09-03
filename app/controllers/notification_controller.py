import importlib

from fastapi import APIRouter
from starlette import status

from app.repositories import user_repository
from app.repositories import notification_repository


router = APIRouter()


def get_channel(channel_name: str):
    if channel_name == 'sms':
        return 'sms'
    if channel_name == 'email':
        return 'email'
    if channel_name == 'push':
        return 'push'
    return 'notification'



@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    dependencies=[]
)
async def post_create(category_id: int, message: str):
    users = user_repository.get_users_by_category(category_id)
    for user in users:
        channels = user.channels.split(",")
        for channel_name in channels:
            channel_type = get_channel(channel_name)
            service = importlib.import_module(f"app.services.{channel_type}_service")
            channel = service.get_channel()
            channel.register_notification(message, user)
    return None


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    dependencies=[]
)
async def get_all():
    return notification_repository.getall()



