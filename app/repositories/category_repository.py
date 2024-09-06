import json

from sqlmodel import Session

from app.models.user import Category
from app.core.database import engine
from app.exceptions.general_exeptions import BadRequestException

class CategoryRepository:
    @staticmethod
    def get_category(id: int) -> Category | None:
        with Session(engine) as session:
            obj = session.get(Category, id)
            return obj

