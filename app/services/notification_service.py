from app.models.user import User


class BaseNotification:
    name: str
    nick: str

    def send_notification(self,user_id:int, message: str):
        user = User(ID=user_id)
        print(f'Sending general notification with: {message} to: {user["name"]}')

def get_service():
    return BaseNotification()

def get_channel(channel_name: str):
    if channel_name == 'sms':
        return 'sms'
    if channel_name == 'email':
        return 'email'
    if channel_name == 'push':
        return 'push'
    return 'notification'
