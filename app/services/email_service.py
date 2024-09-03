from app.services.notification_service import BaseNotification
from app.models.user import User


def get_service():
    return EmailService()


class EmailService(BaseNotification):
    name = 'Email'
    nick = "Email message"

    def send_notification(self, message:str, user: User):
        print(f'Sending email with: {message} to: {user.email}')
