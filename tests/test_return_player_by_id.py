from tests import client

client = client
test_id = 276

def test_get_player_details_by_id(client):
    response = client.get(f"/footballer-pulse/players/{test_id}")
    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)
    assert all(isinstance(player, dict) for player in data)
