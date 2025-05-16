from flask import Flask, request, redirect, render_template, jsonify, send_file
import requests
import os
from dotenv import load_dotenv


# Configure the app
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()
headers = {
'x-rapidapi-key': os.getenv("API_KEY"),
'x-rapidapi-host': 'v3.football.api-sports.io'
}


# Endpoint to return a player details by ID from third-party API.
@app.route("/players/<int:player_id>", methods=["GET"])
def getAllPlayersTest(player_id):

    url = f"https://v3.football.api-sports.io/players/profiles?player={player_id}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        player_info = response.json()
    
        return jsonify(player_info)
    
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch player data", "details": str(e)}), 502

# Endpoint to return a player details by last name from third-party API.
@app.route("/players/<string:player_lastname>", methods=["GET"])
def getPlayerByLastName(player_lastname):

    url = f"https://v3.football.api-sports.io/players/profiles?search={player_lastname}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        player_info = response.json()
    
        return jsonify(player_info)
    
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch player data", "details": str(e)}), 502

# Endpoint to return all player details from third-party API.
@app.route("/players/", methods=["GET"])
def getAllPlayersTestAPI():

    url = f"https://v3.football.api-sports.io/players/profiles"


    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        player_info = response.json()
    
        return jsonify(player_info)
    
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch player data", "details": str(e)}), 502



if __name__ == "__main__":
    # Run the app
    app.run(debug=True)




