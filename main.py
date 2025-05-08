from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv
from interactors.get_player_details import GetPlayerDetailsUseCase
from adapters.football_api_repository import FootballAPIPlayerRepository

app = Flask(__name__)
load_dotenv()
api_key = os.getenv("API_KEY")

# Home screen
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Football API!"


@app.route("/players/<int:player_id>", methods=["GET"])
def get_player_details(player_id):
    repository = FootballAPIPlayerRepository(api_key)
    use_case = GetPlayerDetailsUseCase(repository)

    player_info = use_case.execute(player_id)
    
    return jsonify(player_info)

if __name__ == "__main__":
    app.run(debug=True)

    