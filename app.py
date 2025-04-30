from flask import Flask, redirect, render_template, request, jsonify
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




