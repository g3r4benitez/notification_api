from app.services.notification_service import BaseNotification
from app.models.user import User

def get_service():
    return PushService()


class PushService(BaseNotification):
    name = 'Push'
    nick = "Push message"

    def send_notification(self,user_id:int, message: str):
        user = User(ID=user_id)
        print(f'Sending push with: {message} to: {user["phone_number"]}')
