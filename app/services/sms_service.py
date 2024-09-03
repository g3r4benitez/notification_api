from app.services.notification_service import BaseNotification
from app.models.user import User


def get_service():
    return SmsService()


class SmsService(BaseNotification):
    name = 'Sms'
    nick = "Sms message"

    def send_notification(self, message:str, user: User):
        print(f'Sending sms message with: {message} to: {user.phone_number}')