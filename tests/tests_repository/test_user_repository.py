import pytest
from sqlmodel import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository


@pytest.fixture
def user_repository():
    user_repository = UserRepository()
    return user_repository


def test_create_user(session: Session, user_repository):
    user = User(name="Test create User", email="test@example.com", phone_number=1144223322, channels='sms', subscribed = 'films')
    created_user = user_repository.create(user)
    assert created_user.id is not None
    assert created_user.name == "Test create User"

def test_get_user(session: Session, user_repository):
    user = User(name="Test User", email="test@example.com", phone_number=1144223322, channels='sms', subscribed = 'films')
    user_repository.create(user)
    retrieved_user = user_repository.get(user.id)
    assert retrieved_user is not None
    assert retrieved_user.name == "Test User"

def test_get_all_users(session: Session, user_repository):
    user1 = User(name="User One", email="one@example.com", phone_number=1123993388, channels='sms', subscribed = 'films')
    user2 = User(name="User Two", email="two@example.com", phone_number=1133449933, channels='sms', subscribed = 'films')
    user_repository.create(user1)
    user_repository.create(user2)
    users = user_repository.get_all()
    assert len(users) == 2


def test_remove_user(session: Session):
    user_repository = UserRepository()
    User(name="User to remove", email="remove@example.com", phone_number=1123993388, channels='sms', subscribed = 'films')
    users = user_repository.get_all()
    for user in users:
        print(user.name)
    assert len(users) == 1
    users = user_repository.get_all()
    assert len(users) == 0

