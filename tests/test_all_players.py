from tests import client

client = client

def test_all_footballers_json(client):
    response = client.get('/footballer-pulse/players')
    assert response.status_code == 200
    data = response.get_json()

    assert isinstance(data, list)
    assert all(isinstance(player, dict) for player in data)