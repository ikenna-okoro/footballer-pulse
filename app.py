from flask import Flask, request, redirect, render_template, jsonify, send_file
import requests
import os
from dotenv import load_dotenv
from pprint import pprint
from flask_session import Session

# Configure the app
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()
headers = {
'x-rapidapi-key': os.getenv("API_KEY"),
'x-rapidapi-host': 'v3.football.api-sports.io'
}

# Hardcoded player details
player_data = [
    {
    "id": 1,
    "name": "Roberto Carlos",
    "age": 50,
    "t_shirt_number": 3,
    "position": "Defender",
    },
    {
    "id": 2,
    "name": "Lionel Messi",
    "age": 34,
    "t_shirt_number": 10,
    "position": "Forward",
    },
    {
    "id": 3,
    "name": "Cristiano Ronaldo",
    "age": 36,
    "t_shirt_number": 7,
    "position": "Forward",
    }
]

# Endpoint to return a hardcoded player details.
@app.route("/players", methods=["GET"])
def getAllPlayers():
    return jsonify(player_data)

# Endpoint to return a player details by ID from third-party API.
@app.route("/players/<int:player_id>", methods=["GET"])
def getAllPlayersTest(player_id):

    url = f"https://v3.football.api-sports.io/players/profiles?player={player_id}"

    payload={}
    response = requests.request("GET", url, headers=headers, data=payload)

    player_info = response.json()
    
    return jsonify(player_info)


# @app.route("/players/status", methods=["GET"])
# def getStatus():
#     url = "https://v3.football.api-sports.io/status"
#     payload={}
#     response = requests.request("GET", url, headers=headers, data=payload)
    
#     return(response.json())


# @app.route("/players/photo", methods=["GET"])
# def getPlayerPhoto():
#     player_id = 276
#     if not player_id:
#         return jsonify({"error": "Player ID is required"}), 400

#     url = f"https://media.api-sports.io/football/players/{player_id}.png"
#     response = requests.request("GET", url, headers=headers)
    
#     if response.status_code == 200:
#         from io import BytesIO
#         return send_file(BytesIO(response.content), mimetype='image/png')
#     else:
#         return jsonify({"error": "Failed to fetch image"}), response.status_code    


if __name__ == "__main__":
    # Run the app
    app.run(debug=True)




