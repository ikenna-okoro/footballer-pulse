import pytest

@pytest.fixture
def mock_all_players():
    return {
        "response": [
            {"player": {"id": 1, "name": "Lionel Messi"}},
            {"player": {"id": 2, "name": "Cristiano Ronaldo"}}
        ]
    }

@pytest.fixture
def mock_team_response():
    return {
        "response": [
            {"team": {
                "id": 33, 
                "name": "Manchester United"
                }
            }
        ]
    }

@pytest.fixture
def mock_team_players():
    return {
        "response": [
            {
                "team": {"id": 33},
                "players": [
                    {"id": 1, "name": "Marcus Rashford"},
                    {"id": 2, "name": "Bruno Fernandes"}
                ]
            }
        ]
    }