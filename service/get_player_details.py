from domain.player import Player
from repository.football_api_repository import FootballAPIPlayerRepository


# Interactor (use case) for getting player details
class GetPlayerDetailsUseCase:

    # Constructor that takes a PlayerRepository instance object
    def __init__(self):
        self.repository = FootballAPIPlayerRepository()

    # Method to execute the use case
    def execute_by_name(self, player_name: str) -> Player:
        return self.repository.get_player_by_name(player_name)
    
    # Method to execute the use case
    def execute_by_id(self, player_id: int) -> Player:
        return self.repository.get_player_by_id(player_id)