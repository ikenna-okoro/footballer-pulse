from entities.player import Player

# Interface for the PlayerRepository
class PlayerRepository():

    def get_player_by_id(self, player_id: int) -> Player:
        ...
    
    def get_player_by_name(self, player_name: str) -> Player:
        ...