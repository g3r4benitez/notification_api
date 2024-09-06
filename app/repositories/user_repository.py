from app.models.user import User
from app.repositories.base_respository import BaseRepository

class UserRepository(BaseRepository):
    model_name = User


user_repository = UserRepository()