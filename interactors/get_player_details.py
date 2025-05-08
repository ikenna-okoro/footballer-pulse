from typing import Protocol
from entities.player import Player

class PlayerRepository(Protocol):

    def get_player_by_id(self, player_id: int) -> Player:
        ...

class GetPlayerDetailsUseCase:

    def __init__(self, repository: PlayerRepository):
        self.repository = repository


    def execute(self, player_id: int) -> Player:
        return self.repository.get_player_by_id(player_id)
    