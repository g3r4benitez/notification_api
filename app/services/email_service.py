from app.services.notification_service import BaseNotification
from app.repositories import user_repository


def get_channel():
    return EmailService()


class EmailService(BaseNotification):
    name = 'Email'
    nick = "Email message"
