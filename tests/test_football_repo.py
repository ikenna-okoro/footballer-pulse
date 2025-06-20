from repository.football_repo import FootBallRepository, Player
import pytest
from unittest.mock import patch
from domain.player import Player
from domain.team import Team


# Test response for all players
def test_get_all_players(mock_all_players):
    repo = FootBallRepository()
    
    with patch.object(repo, "_make_request", return_value=mock_all_players):
        result = repo.get_all_players()

        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(p, Player) for p in result)
        assert result[0].name == "Lionel Messi"

# Test response for player by last name
def test_get_player_by_lastname(mock_all_players):
    repo = FootBallRepository()
    
    with patch.object(repo, "_make_request", return_value=mock_all_players):
        result = repo.get_player_by_lastname("Messi")
        
        assert len(result) == 2
        assert result[0].name == "Lionel Messi"

# Test response for player by ID
def test_get_player_by_id(mock_all_players):
    repo = FootBallRepository()
    
    with patch.object(repo, "_make_request", return_value=mock_all_players):
        result = repo.get_player_by_id(1)
        
        assert isinstance(result[0], Player)
        assert len(result) == 2
        assert result[0].id == 1

# Test response for players in a team
def test_get_players_in_team(mock_team_players):
    repo = FootBallRepository()
    
    with patch.object(repo, "_make_request", return_value=mock_team_players):
        result = repo.get_players_in_team(33)
        
        assert isinstance(result, list)
        assert len(result) == 2
        assert isinstance(result[0], Player)
        assert result[0].name == "Marcus Rashford"

# Test response for team details by ID
def test_get_team_details_by_id(mock_team_response):
    repo = FootBallRepository()
    
    with patch.object(repo, "_make_request", return_value=mock_team_response):
        result = repo.get_team_details_by_id("33")

        assert len(result) == 1
        assert isinstance(result[0], Team)
        assert result[0].name == "Manchester United"