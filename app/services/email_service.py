from app.services.notification_service import BaseNotification
from app.models.user import User


def get_service():
    return EmailService()


class EmailService(BaseNotification):
    name = 'Email'
    nick = "Email message"

    def send_notification(self, user_id: int, message:str):
        user = User(ID=user_id)
        print(f'Sending email with: {message} to: {user["email"]}')
