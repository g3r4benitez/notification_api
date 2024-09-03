from app.services.notification_service import BaseNotification
from app.repositories import user_repository


def get_channel():
    return SmsService()


class SmsService(BaseNotification):
    name = 'Sms'
    nick = "Sms message"
