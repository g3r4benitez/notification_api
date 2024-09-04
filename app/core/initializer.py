from typing import Dict
import glob
import sys
from os.path import dirname, basename, isfile
from dependency_injector.containers import DynamicContainer
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from app.core.config import DB_URL
from app.core.containers import (ContainerService)
from app import controllers
from app.repositories.user_repository import UserRepository, user_repository
from app.models.user import User



def init(app: FastAPI):
    """Load 3rd parties libs init config, After FastApi"""
    __fill_db()
    app.containers = start_containers()




def __fill_db():
    users_json = UserRepository.get_users_from_json()
    for user_json in users_json:
        user = UserRepository.get_user(user_id=user_json['id'])
        if user is None:
            user = User()
            user.id = user_json['id']
            user.name = user_json['name']
            user.email = user_json['email']
            user.phone_number = user_json['phone_number']
            user.subscribed = ",".join(user_json['subscribed'])
            user.channels = ",".join(user_json['channels'])
            user_repository.create_user(user)



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
