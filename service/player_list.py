from repository.player_repo import PlayerRepository

class GetPlayerDetailsUseCase:
    def __init__(self):
        self.player_repo = PlayerRepository()

    def player_list_use_case(self):
        return self.player_repo.get_all_players()

    def player_list_by_name_use_case(self, lastname):
        return self.player_repo.get_player_by_lastname(lastname)

    def player_list_by_id_use_case(self, player_id):
        return self.player_repo.get_player_by_id(player_id)