from app.services.notification_service import BaseNotification
from app.models.user import User


def get_service():
    return SmsService()


class SmsService(BaseNotification):
    name = 'Sms'
    nick = "Sms message"

    def send_notification(self,user_id:int, message: str):
        user = User(ID=user_id)
        print(f'Sending sms message with: {message} to: {user["phone_number"]}')