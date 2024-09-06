import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.user import User
from app.repositories.user_repository import UserRepository

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def mock_user_service(mocker):
    return mocker.patch("app.repositories.user_repository.UserRepository")

@pytest.fixture
def user_repository(mocker):
    return mocker.Mock(UserRepository)


def test_send_notification(client, user_repository, mocker):
    user = User(id=1, name="Test User", email="test@example.com", phone_number=1133993344, channels='sms', subscribed = 'films')
    user_repository.get_all.return_value = [user]
    mock_send_notification_task = mocker.patch("app.controllers.notification_controller.send_notification_task.delay")
    response = client.post("/api/notification",json = {"category": "films","message": "hola mundo"} )
    assert response.status_code == 201
    assert response.json() ==  {'category': 'films', 'message': 'hola mundo'}
    #mock_send_notification_task.assert_called_once_with(user.id, user.id, "hola mundo", "sms")

