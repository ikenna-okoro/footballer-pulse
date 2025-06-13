from tests import client

client = client
def test_home_page(client):
    response = client.get('/footballer-pulse/')
    assert response.status_code == 200
    assert b'Welcome to the Football-Pulse!' in response.data
