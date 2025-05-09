from flask import Flask, jsonify
from flask import Blueprint
import os
from dotenv import load_dotenv
from interactors.get_player_details import GetPlayerDetailsUseCase
from adapters.football_api_repository import FootballAPIPlayerRepository

bp = Blueprint('my_blueprint', __name__)
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Home screen
@bp.route("/", methods=["GET"])
def homePage():
    return "<h1> Welcome to the Football-Pulse!</h1><p> This is a simple API to get player details.</p>"
    

@bp.route("/players/<int:player_id>", methods=["GET"])
def get_player_details(player_id):
    # request model
    player_repository = FootballAPIPlayerRepository(API_KEY)
    use_case = GetPlayerDetailsUseCase(player_repository)
    
    # response model
    player_info = use_case.execute(player_id)
    
    return jsonify(player_info)

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.run(debug=True)

    