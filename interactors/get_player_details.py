from typing import Protocol
from entities.player import Player

# Interface for the PlayerRepository
class PlayerRepository(Protocol):

    def get_player_by_id(self, player_id: int) -> Player:
        ...
    
    def get_player_by_name(self, player_name: str) -> Player:
        ...

# Interactor (use case) for getting player details
class GetPlayerDetailsUseCase:

    # Constructor that takes a PlayerRepository instance object
    def __init__(self, repository: PlayerRepository):
        self.repository = repository

    # Method to execute the use case
    def execute(self, player_id: int) -> Player:
        return self.repository.get_player_by_id(player_id)
 