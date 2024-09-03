from sqlalchemy.exc import IntegrityError
from fastapi_sqlalchemy import db

from app.models import category as models
from app.models.orm import category as orm
from app.exceptions.general_exeptions import ConflictExeption


def get(name: str):
    return db.session.query(orm.Category).filter(orm.Category.name == name).first()


def create(category: models.Category):
    try:
        entity = orm.Category(**category.dict())
        db.session.add(entity)
        db.session.commit()
        return entity
    except IntegrityError as error:
        raise ConflictExeption("Category already exists")


def getall():
    return db.session.query(orm.Category).all()

