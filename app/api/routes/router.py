from fastapi import APIRouter

from app.controllers import user_controller as user
from app.controllers import subscription_controller as subscription
from app.controllers import channel_controller as channel
from app.controllers import notification_controller as notification
from app.controllers import ping_controller as ping
from app.core.config import API_PREFIX

api_router = APIRouter(prefix=API_PREFIX)
api_router.include_router(user.router, tags=["user"], prefix="/api/user")
api_router.include_router(subscription.router, tags=["subscription"], prefix="/api/subscription")
api_router.include_router(channel.router, tags=["channel"], prefix="/api/channel")
api_router.include_router(notification.router, tags=["notification"], prefix="/api/notification")
api_router.include_router(ping.router, tags=["ping"], prefix="/api/ping")


