import pytest
from sqlmodel import create_engine, SQLModel, Session
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import get_session

# Crear una base de datos en memoria para pruebas
@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")  # Base de datos en memoria
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

# Sobrescribir la dependencia de la sesión de base de datos para usar la base de datos en memoria
@pytest.fixture(autouse=True)
def override_get_session(session: Session):
    def _get_session_override():
        return session
    app.dependency_overrides[get_session] = _get_session_override
    yield
    app.dependency_overrides.clear()