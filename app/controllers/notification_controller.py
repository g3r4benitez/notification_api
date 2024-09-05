from pyexpat.errors import messages

from fastapi import APIRouter
from starlette import status

from app.repositories import notification_repository
from app.models.notification import Notification
from app.core.celery_worker import send_notification_task
from app.repositories.user_repository import UserRepository
from app.core.error_handler import HTTPCustomException, status
from app.core.logger import logger

router = APIRouter()

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    dependencies=[]
)
async def send_notification_by_category(notification: Notification):
    users = UserRepository.get_users()
    try:
        for user in users:
            print(user)
            if notification.category in user.subscribed.split(','):
                channels = user.channels.split(',')
                for channel_name in channels:
                    send_notification_task.delay(user.id, notification.message, channel_name)
    except Exception as e:
        logger.error(f"Error during send notification: {e}")
        raise HTTPCustomException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, msg='Internal server error')

    return notification


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    dependencies=[]
)
async def get_all():
    return notification_repository.getall()



