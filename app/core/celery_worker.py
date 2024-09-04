import importlib
from celery.utils.log import get_task_logger

from .celery_app import celery_app
from app.services.notification_service import get_channel
from app.repositories.user_repository import UserRepository

celery_log = get_task_logger(__name__)

@celery_app.task(
    name='app.core.celery_worker.send_notification_task',
    queue="report_tabs",
    max_retries=10,
    default_retry_delay=60
)
def send_notification_task(user_id: int, message: str, channel_name: str,  ):
    user = UserRepository.get_user(user_id)
    celery_log.info(f"a log message")
    channel_type = get_channel(channel_name)
    channel_service = importlib.import_module(f"app.services.{channel_type}_service")
    service_notification = channel_service.get_service()
    service_notification.send_notification(user, message)