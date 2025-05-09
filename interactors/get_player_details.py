from typing import Protocol
from entities.player import Player

# Interface for the PlayerRepository
class PlayerRepository(Protocol):

    def get_player_by_id(self, player_id: int) -> Player:
        ...

# Interactor (use case) for getting player details
# This class is responsible for the business logic of retrieving player details
# It uses the PlayerRepository to fetch player data
# and returns the player details in a structured format
class GetPlayerDetailsUseCase:

    def __init__(self, repository: PlayerRepository):
        self.repository = repository

    # Method to execute the use case (interactor uses the repository to get player details and return them)
    def execute(self, player_id: int) -> Player:
        return self.repository.get_player_by_id(player_id)
 