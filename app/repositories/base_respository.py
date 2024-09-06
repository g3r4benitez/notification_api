import json

from sqlmodel import Session, select, SQLModel

from app.models.user import User
from app.core.database import engine
from app.exceptions.general_exeptions import BadRequestException

class BaseRepository:
    model_name = SQLModel

    @classmethod
    def get(cls, id: int):
        with Session(engine) as session:
            obj =  session.get(cls.model_name, id)
            return obj

    @classmethod
    def remove_user(cls, id: int) -> None:
        with Session(engine) as session:
            obj = cls.get(id)
            if not obj:
                raise BadRequestException(message='user not found')
            session.delete(obj)
            session.commit()
            session.refresh(obj)

    @classmethod
    def create(cls, obj: SQLModel):
        with Session(engine) as session:
            session.add(obj)
            session.commit()
            session.refresh(obj)
        return obj

    @classmethod
    def get_all(cls) -> [SQLModel]:
        with Session(engine) as session:
            statement = select(cls.model_name)
            results = session.exec(statement)
            return results.all()

