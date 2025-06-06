from flask import Flask, Blueprint
from repository.player_repo import PlayerRepository
from service.player_list import GetPlayerDetailsUseCase


bp = Blueprint('my_blueprint', __name__)

player_repository = PlayerRepository()
use_case = GetPlayerDetailsUseCase(player_repository)


# Home screen
@bp.route("/", methods=["GET"])
def homePage():
    return "<h1> Welcome to the Football-Pulse!</h1><p> This is a simple API to get player details.</p>"


# Return all players
@bp.route("/players", methods=["GET"])
def get_all_players():
    return [player.to_dict() for player in use_case.player_list_use_case()]


# Return player by name
@bp.route("/players/name/<string:lastname>", methods=["GET"])
def get_player_by_name(lastname):
    use_case_by_name = use_case.player_list_by_name_use_case(lastname)
    if not use_case_by_name:
        return {"error": "Player not found"}, 404
    return [player.to_dict() for player in use_case_by_name]


# Return player by id
@bp.route("/players/id/<int:player_id>", methods=["GET"])
def get_player_by_id(player_id):
    use_case_by_id = use_case.player_list_by_id_use_case(player_id)
    if not use_case_by_id:
        return {"error": "Player not found"}, 404
    return [player.to_dict() for player in use_case_by_id]

# Return players by team
@bp.route("/players/team/<int:team_id>", methods=["GET"])
def get_players_by_team(team_id):
    use_case_by_team = use_case.player_list_by_team_use_case(team_id)
    if not use_case_by_team:
        return {"error": "Team not found"}, 404
    return [player.to_dict() for player in use_case_by_team]


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.run(debug=True)