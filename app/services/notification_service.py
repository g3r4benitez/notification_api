from app.models.notification import Notification
from app.repositories import notification_repository
from app.models.user import User
from datetime import datetime


class BaseNotification:
    name: str
    nick: str

    def send_notification(self, message, user):
        pass

    def register_notification(self, message: str, user: User):
        message = f"Sending a message:'{message}', to: {user.name}"
        obj_notification = Notification(message=message, channel=self.name, date_creation=datetime.now())
        notification_repository.create(notification=obj_notification)


