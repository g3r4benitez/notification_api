import os
from celery import Celery
from celery.signals import after_setup_task_logger
from celery.app.log import TaskFormatter
from app.core.config import CELERY_BROKER_URL

celery = Celery("task", broker='amqp://guest:guest@localhost:5672//')

celery_app = Celery(
    "worker",
    broker='amqp://guest:guest@localhost:5672//'
)


celery_app.conf.update(task_track_started=True)

@after_setup_task_logger.connect
def setup_task_logger(logger, *args, **kwargs):
    for handler in logger.handlers:
        handler.setFormatter(TaskFormatter('%(asctime)s - %(task_id)s - %(task_name)s - %(name)s - %(levelname)s - %(message)s'))

