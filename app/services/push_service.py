from app.services.notification_service import BaseNotification


def get_channel():
    return PushService()


class PushService(BaseNotification):
    name = 'Push'
    nick = "Push message"
