from fastapi import APIRouter
from starlette import status

from app.repositories import user_repository
from app.repositories import notification_repository
from app.services.notification_service import get_channel
from app.models.user import User
from app.models.notification import Notification
from app.core.celery_worker import send_notification_task

router = APIRouter()

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    dependencies=[]
)
async def send_by_category(notification: Notification):
    users = user_repository.get_users()

    for user in users:
        # obj_user = User(**user)
        if notification.category in user['subscribed']:
            channels = user['channels']
            for channel_name in channels:
                send_notification_task(user['ID'], notification.message, channel_name)
                #send_notification_task.delay(user['ID'], notification.message, channel_name)

    return notification


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    dependencies=[]
)
async def get_all():
    return notification_repository.getall()



