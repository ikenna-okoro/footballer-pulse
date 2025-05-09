from flask import Flask, jsonify
import os
from dotenv import load_dotenv
from interactors.get_player_details import GetPlayerDetailsUseCase
from adapters.football_api_repository import FootballAPIPlayerRepository

app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Home screen
@app.route("/", methods=["GET"])
def homePage():
    return "<h1> Welcome to the Football-Pulse!</h1><p> This is a simple API to get player details.</p>"
    

@app.route("/players/<int:player_id>", methods=["GET"])
def get_player_details(player_id):
    player_repository = FootballAPIPlayerRepository(API_KEY)
    use_case = GetPlayerDetailsUseCase(player_repository)

    player_info = use_case.execute(player_id)
    
    return jsonify(player_info)

if __name__ == "__main__":
    app.run(debug=True)

    