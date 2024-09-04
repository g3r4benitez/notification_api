import pytest
from sqlmodel import Session
from app.models.user import User
from app.repositories.user_repository import UserRepository

@pytest.fixture
def session_test():
    from sqlmodel import create_engine
    from sqlmodel import SQLModel

    engine_test = create_engine("sqlite:///:memory:", echo=True)
    SQLModel.metadata.create_all(engine_test)
    with Session(engine_test) as session_test:
        yield session_test

@pytest.fixture
def user_repository(session_test):
    return UserRepository()

def test_create_user(user_repository):
    user = User(name="Test User", email="test@example.com", phone_number=1144223322)
    created_user = user_repository.create_user(user)
    assert created_user.id is not None
    assert created_user.name == "Test User"

def test_get_user(user_repository):
    user = User(name="Test User", email="test@example.com", phone_number=1144223322)
    user_repository.create_user(user)
    retrieved_user = user_repository.get_user(user.id)
    assert retrieved_user is not None
    assert retrieved_user.name == "Test User"

def test_get_all_users(user_repository):
    user1 = User(name="User One", email="one@example.com", phone_number=1123993388)
    user2 = User(name="User Two", email="two@example.com", phone_number=1133449933)
    user_repository.create_user(user1)
    user_repository.create_user(user2)
    users = user_repository.get_users()
    assert len(users) == 2

def test_remove_user(user_repository):
    user1 = User(name="User One", email="one@example.com", phone_number=1123993388)
    users = user_repository.get_users()
    assert len(users) == 1
    user_repository.remove_user(user1.id)
    users = user_repository.get_users()
    assert len(users) == 0

