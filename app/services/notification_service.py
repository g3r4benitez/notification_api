from app.models.user import User


class BaseNotification:
    name: str
    nick: str

    def send_notification(self, message: str, user: User):
        print(f'Sending general notification with: {message} to: {user.name}')

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
