from fastapi import APIRouter
from starlette import status

from app.models.user import User
from app.repositories import user_repository


router = APIRouter()


@router.post(
    "",
    name="user_create",
    status_code=status.HTTP_201_CREATED,
    dependencies=[]
)
async def post_create(user: User):
    user = user_repository.create(user)
    return user

@router.get(
    "",
    name="user_getall",
    status_code=status.HTTP_200_OK,
    dependencies=[]
)
async def get_user():
    return user_repository.getall()

@router.get(
    "/{email}",
    name="user_get",
    status_code=status.HTTP_200_OK,
    dependencies=[]
)
async def get_user(email: str):
    return user_repository.get(email)

@router.patch(
    "/{user_email}",
    name="user_update",
    status_code=status.HTTP_200_OK,
    dependencies=[]
)
async def update_user(user: User, user_email: str):
    user_db = user_repository.update(user_email, user)
    return user_db
