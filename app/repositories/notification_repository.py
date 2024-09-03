from fastapi_sqlalchemy import db

from app.models import notification as models
from app.models.orm import notification as orm


def create(notification: models.Notification):
    entity = orm.Notification(**notification.dict())
    db.session.add(entity)
    db.session.commit()
    return entity


def getall():
    return db.session.query(orm.Notification).order_by(orm.Notification.date_creation.desc()).all()


