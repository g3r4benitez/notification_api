from fastapi import APIRouter
from starlette import status

from app.repositories import user_repository
from app.repositories import notification_repository
from app.models.notification import Notification
from app.core.celery_worker import send_notification_task
from app.repositories.user_repository import UserRepository

router = APIRouter()

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    dependencies=[]
)
async def send_by_category(notification: Notification):
    users = UserRepository.get_users()

    for user in users:
        if notification.category in user.subscribed.split(','):
            channels = user.channels.split(',')
            for channel_name in channels:
                send_notification_task.delay(user.id, notification.message, channel_name)

    return notification


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    dependencies=[]
)
async def get_all():
    return notification_repository.getall()



