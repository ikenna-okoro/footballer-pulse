from flask import Flask, redirect, render_template, jsonify
import requests
import os
from dotenv import load_dotenv
from pprint import pprint
from flask_session import Session

# Configure the app
app = Flask(__name__)

# Hardcoded player details
player_data = {
    "id": 1,
    "name": "Roberto Carlos",
    "age": 50,
    "t_shirt_number": 3,
    "position": "Defender",
}

# Endpoint to return a hardcoded player details.
@app.route("/players", methods=["GET"])
def getAllPlayers():
    return jsonify(player_data)

@app.route("/players/test", methods=["GET"])
def getAllPlayersTest():

    url = "https://v3.football.api-sports.io/players/profiles?player=276"

    payload={}
    load_dotenv()
    headers = {
    'x-rapidapi-key': os.getenv("API_KEY"),
    'x-rapidapi-host': 'v3.football.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    pprint(response.json())


    
    return jsonify(player_data)




