from controller import create_app
import pytest



@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_homepage_route(client):
    response = client.get("/footballer-pulse/")
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"Home_message": "Welcome to the Football-Pulse! This is a simple API to get player details"}