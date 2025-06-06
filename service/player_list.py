from repository.football_repo import PlayerRepository

class PlayerDetailsUseCase:
    def __init__(self, player_repo: PlayerRepository):
        self.player_repo = player_repo

    def player_list_use_case(self):
        return self.player_repo.get_all_players()

    def player_list_by_name_use_case(self, lastname):
        return self.player_repo.get_player_by_lastname(lastname)

    def player_list_by_id_use_case(self, player_id):
        return self.player_repo.get_player_by_id(player_id)
    
    def player_list_by_team_use_case(self, team_id):
        return self.player_repo.get_players_by_team(team_id)

