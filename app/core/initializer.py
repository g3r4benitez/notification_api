from typing import Dict
import glob
import sys
from os.path import dirname, basename, isfile
from dependency_injector.containers import DynamicContainer
from fastapi import FastAPI

from app.core.containers import (ContainerService)
from app import controllers
from app.repositories.user_repository import UserRepository, user_repository
from app.models.user import User, Channel, Subscription

from app.services.user_service import user_service
from app.services.initializer_service import InitializerService
from app.services.channel_service import channel_service
from app.services.subscription_service import subscription_service
from app.core.logger import logger



def init(app: FastAPI):
    """Load 3rd parties libs init config, After FastApi"""
    app.containers = start_containers()
    __fill_db()




def __fill_db():
    channels_json = InitializerService.get_channels_from_json()

    for channel_json in channels_json:
        channel = channel_service.get(_id=channel_json['id'])
        logger.info(channel)
        if channel is None:
            channel = Channel()
            channel.id = channel_json['id']
            channel.name = channel_json['name']
            channel_service.create_channel(channel)
            logger.info(f'Creating channel: {channel.name}')


    subscriptions_json = InitializerService.get_subscriptions_from_json()
    logger.info(subscriptions_json)
    for subscriptions_json in subscriptions_json:
        subscription = subscription_service.get(_id=subscriptions_json['id'])
        if subscription is None:
            subscription = Subscription()
            subscription.id = subscriptions_json['id']
            subscription.name = subscriptions_json['name']
            subscription_service.create_subscription(subscription)
            logger.info(f'Creating subscription: {subscription.name}')

    users_json = InitializerService.get_users_from_json()
    for user_json in users_json:
        user = UserRepository.get(id=user_json['id'])
        if user is None:
            user = User()
            user.id = user_json['id']
            user.name = user_json['name']
            user.email = user_json['email']
            user.phone_number = user_json['phone_number']
            user_service.create_user(user)
            logger.info(f'Creating user: {user.name}')
            for u_subscription in user_json['subscriptions']:
                user_service.add_subscription_to_user(user.id, u_subscription)
                logger.info(f'Creating user-subscription: user_id:{user.id}, subscription_id: {u_subscription}')
            for u_channel in user_json['channels']:
                user_service.add_channels_to_user(user.id, u_channel)
                logger.info(f'Creating user-channel: user_id:{user.id}, subscription_id: {u_channel}')



def start_containers() -> Dict[str, DynamicContainer]:
    """
    wire the containers declared in 'containers' list with the
    controllers located in 'from app import controllers'.
    """
    containers: Dict[str, ...] = {
        "service_container": ContainerService(),
    }

    paths = glob.glob(dirname(controllers.__file__) + "/*.py")
    modules = [f"{controllers.__name__}.{basename(f)[:-3]}"
               for f in paths if isfile(f) and not f.endswith('__init__.py')]
    for container in containers.values():
        container.wire(modules=[sys.modules[m] for m in modules])
    return containers
