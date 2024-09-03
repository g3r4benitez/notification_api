from sqlalchemy.exc import IntegrityError
from fastapi_sqlalchemy import db

from app.models import user as models
from app.models.orm import user as orm
from app.exceptions.general_exeptions import ConflictExeption


def get(_id: int):
    return db.session.query(orm.User).filter(orm.User.id == _id).first()


def create(user: models.User):
    try:
        entity = orm.User(**user.dict())
        db.session.add(entity)
        db.session.commit()
        return entity
    except IntegrityError as error:
        raise ConflictExeption("Email in use")


def get(email: str):
    return db.session.query(orm.User).filter(orm.User.email == email).first()


def getall():
    return db.session.query(orm.User).all()


def get_users_by_category(category_id):
    # Here I have to return users related with categories
    # todo: resolve filter by category_id
    return db.session.query(orm.User).all()


def update(email: str, obj_user: models.User):
    user = db.session.query(orm.User).filter(orm.User.email == email).first()
    user.name = obj_user.name
    user.phone_number = obj_user.phone_number
    user.channels = obj_user.channels
    db.session.commit()
    return user




