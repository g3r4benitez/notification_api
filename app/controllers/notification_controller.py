from pyexpat.errors import messages

from fastapi import APIRouter, Depends

from app.models.notification import Notification
from app.core.celery_worker import send_notification_task
from app.repositories.user_repository import UserRepository
from app.core.error_handler import HTTPCustomException, status
from app.core.logger import logger
from app.services.user_service import user_service
from app.services.subscription_service import subscription_service

router = APIRouter()

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    dependencies=[],
    response_model=Notification
)
async def send_notification_by_category(notification: Notification):
    users = UserRepository.get_all()
    try:
        for user in users:
            user_subscriptions = user_service.get_user_subscriptions(user.id)
            suscriptions_ids = list(map(lambda s: s.id, user_subscriptions))
            logger.info(suscriptions_ids)
            subscription = subscription_service.get_by_name(notification.category)
            if subscription and subscription.id in suscriptions_ids:
                channels = user_service.get_user_channels(user.id)
                for channel in channels:
                    send_notification_task.delay(user.id, notification.message, channel.name)
    except Exception as e:
        logger.error(f"Error during send notification: {e}")
        raise HTTPCustomException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, msg='Internal server error')

    return notification

