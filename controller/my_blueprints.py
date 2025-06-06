from flask import Flask, Blueprint, jsonify, request
from repository.football_repo import FootBallRepository
from repository.fan_comment_repo import CommentRepository
from repository.fan_models import FansComment
from service.player_list import PlayerDetailsUseCase
from service.team_list import TeamDetailsUseCase 
from service.fans_comment import FansCommentUseCase


bp = Blueprint('my_blueprint', __name__)

player_repository = FootBallRepository()
use_case = PlayerDetailsUseCase(player_repository)
all_players = use_case.player_list_use_case()
players_by_name = use_case.player_list_by_name_use_case()
players_by_id = use_case.player_list_by_id_use_case()
players_in_team = use_case.player_list_in_team_use_case()

team_repository = FootBallRepository()
team_details_use_case = TeamDetailsUseCase(team_repository)

comment_repository = CommentRepository()
fans_comment_use_case = FansCommentUseCase(comment_repository)


# Home screen
@bp.route("/", methods=["GET"])
def homePage():
    return "<h1> Welcome to the Football-Pulse!</h1><p> This is a simple API to get player details.</p>"


# Return all players
@bp.route("/players", methods=["GET"])
def get_all_players():
    return [player.to_dict() for player in all_players]


# Return player by name
@bp.route("/players/<string:lastname>", methods=["GET"])
def get_player_by_name():

    if not players_by_name:
        return {"error": "Player not found"}, 404
    return [player.to_dict() for player in players_by_name]


# Return player by id
@bp.route("/players/<int:player_id>", methods=["GET"])
def player_details_by_id(player_id):
    if not players_by_id:
        return {"error": "Player not found"}, 404
    return [player.to_dict() for player in players_by_id]

# Return players in a team (Squad)
@bp.route("/players/team/<int:team_id>", methods=["GET"])
def get_players_by_team():
    if not players_in_team:
        return {"error": "Team not found"}, 404
    return [player.to_dict() for player in players_in_team]

# Fans comments for a specific team
@bp.route("/teams/<int:team_id>", methods=["GET", "POST"])
def team_details_for_fans(team_id):
    usecase_by_team_details = team_details_use_case.team_details_use_case(team_id)
    if not usecase_by_team_details:
        return {"error": "Team not found"}, 404
    team_name = usecase_by_team_details[0].name

    if request.method == "POST":
        team = team_name
        data = request.get_json()
        if request.content_type != 'application/json':
            return {"error": "Content-Type must be application/json"}, 400
        username = data.get('username')
        comment = data.get('comment')

        if not all([username, comment]):
            return {"error": "Missing user data fields"}, 400

        return fans_comment_use_case.save_fans_comment_to_db(team, username, comment)

    # If GET request, return all comments for a specific team
    
    if not usecase_by_team_details:
        return {"error": "Team not found"}, 404
    team_data = [team.to_dict() for team in usecase_by_team_details]
    comments_data = [comment.to_dict() for comment in FansComment.query.filter_by(team_name=team_name).all()]

    return jsonify({    
        "team": team_data,
        "comments": comments_data
    })
