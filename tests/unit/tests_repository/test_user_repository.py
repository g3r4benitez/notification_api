import pytest
from sqlmodel import Session
from app.models.user import User
from app.repositories.user_repository import UserRepository

@pytest.fixture
def session():
    # Aquí podrías usar una base de datos en memoria para pruebas
    from sqlmodel import create_engine
    from sqlmodel import SQLModel

    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.fixture
def user_repository(session):
    return UserRepository(session)

def test_create_user(user_repository):
    user = User(name="Test User", email="test@example.com")
    created_user = user_repository.create_user(user)
    assert created_user.id is not None
    assert created_user.name == "Test User"

def test_get_user(user_repository):
    user = User(name="Test User", email="test@example.com")
    user_repository.create_user(user)
    retrieved_user = user_repository.get_user(user.id)
    assert retrieved_user is not None
    assert retrieved_user.name == "Test User"

def test_get_all_users(user_repository):
    user1 = User(name="User One", email="one@example.com")
    user2 = User(name="User Two", email="two@example.com")
    user_repository.create_user(user1)
    user_repository.create_user(user2)
    users = user_repository.get_all_users()
    assert len(users) == 2
