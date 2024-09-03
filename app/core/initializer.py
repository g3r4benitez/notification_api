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


def init(app: FastAPI):
    """Load 3rd parties libs init config, After FastApi"""
    __init_db(app)
    app.containers = start_containers()


def __init_db(app: FastAPI):
    app.add_middleware(DBSessionMiddleware, db_url=DB_URL, engine_args={})


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
