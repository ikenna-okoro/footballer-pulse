from repository.football_repo import FootBallRepository
class TeamDetailsUseCase:
    def __init__(self, player_repo: FootBallRepository):
        self.player_repo = player_repo

    def team_details_use_case(self, team_id):
        return self.player_repo.get_players_in_team(team_id)