from flask import Flask
from flask import Blueprint
from interactors.get_player_details import GetPlayerDetailsUseCase


bp = Blueprint('my_blueprint', __name__)
use_case = GetPlayerDetailsUseCase()


# Home screen
@bp.route("/", methods=["GET"])
def homePage():
    return "<h1> Welcome to the Football-Pulse!</h1><p> This is a simple API to get player details.</p>"
    
# Endpoint to return a player details by lastname from third-party API.
@bp.route("/players/name/<string:player_name>", methods=["GET"])
def get_player_details_by_name(player_name):
    
    player_info = use_case.execute_by_name(player_name)

    return player_info

# Endpoint to return a player details by id from third-party API.
@bp.route("/players/id/<int:player_id>", methods=["GET"])
def get_player_details_by_id(player_id):
    
    player_info = use_case.execute_by_id(player_id)

    return player_info 

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.run(debug=True)   