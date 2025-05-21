import requests
from dotenv import load_dotenv
import os
from domain.player import Player

class PlayerRepository:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")


    def get_all_players(self):
        url = f"https://v3.football.api-sports.io/players/profiles"
        headers = {
        'x-apisports-key': self.api_key,
        'x-rapidapi-host': 'v3.football.api-sports.io'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error fetching player data: {response.status_code}")

        player_data = response.json()

        return [Player.from_dict(player['player']) for player in player_data['response']]


    def get_player_by_lastname(self, lastname: str):
        url = f"https://v3.football.api-sports.io/players/profiles?search={lastname}"
        headers = {
        'x-apisports-key': self.api_key,
        'x-rapidapi-host': 'v3.football.api-sports.io'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error fetching player data: {response.status_code}")

        player_data = response.json()

        return [Player.from_dict(player['player']) for player in player_data['response']]


    def get_player_by_id(self, player_id: int):
        url = f"https://v3.football.api-sports.io/players/profiles?player={player_id}"
        headers = {
        'x-apisports-key': self.api_key,
        'x-rapidapi-host': 'v3.football.api-sports.io'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error fetching player data: {response.status_code}")

        player_data = response.json()

        return [Player.from_dict(player['player']) for player in player_data['response']]     