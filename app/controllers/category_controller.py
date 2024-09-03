from fastapi import APIRouter
from starlette import status

from app.models.category import Category
from app.repositories import category_repository


router = APIRouter()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    dependencies=[]
)
async def post_create(category: Category):
    category = category_repository.create(category)
    return category


@router.get(
    "/{category_name}",
    status_code=status.HTTP_200_OK,
    dependencies=[]
)
async def get_category(category_name: str):
    return category_repository.get(category_name)


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    dependencies=[]
)
async def get_all():
    return category_repository.getall()
