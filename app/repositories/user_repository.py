import json
from sqlmodel import Session, select

from app.models.user import User
from app.core.database import engine


class UserRepository:

    @staticmethod
    def get_user(user_id: int) -> User | None:
        with Session(engine) as session:
            user =  session.get(User, user_id)
            return user

    def create_user(self, user: User):
        with Session(engine) as session:
            session.add(user)
            session.commit()
            session.refresh(user)
        return user

    @staticmethod
    def get_users():
        with Session(engine) as session:
            statement = select(User)
            results = session.exec(statement)
            return results.all()

    @staticmethod
    def get_users_from_json():
        with open('app/data/users.json', 'r') as file:
            data = json.load(file)
            return data['users']

user_repository = UserRepository()