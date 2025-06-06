import requests
from flask import request
from dotenv import load_dotenv
import os
from domain.player import Player
from domain.team import Team


class FootBallRepository:
    def __init__(self, player_id:int = None, team_id:int = None, lastname:str = None):
        self.player_id = player_id
        self.team_id = team_id
        self.lastname = lastname
        # Load environment variables from .env file
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

    def get_player_by_lastname(self):
        url = f"https://v3.football.api-sports.io/players/profiles?search={self.lastname}"
        headers = {
        'x-apisports-key': self.api_key,
        'x-rapidapi-host': 'v3.football.api-sports.io'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error fetching player data: {response.status_code}")

        player_data = response.json()

        return [Player.from_dict(player['player']) for player in player_data['response']]


    def get_player_by_id(self):

        url = f"https://v3.football.api-sports.io/players/profiles?player={self.player_id}"
        headers = {
        'x-apisports-key': self.api_key,
        'x-rapidapi-host': 'v3.football.api-sports.io'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error fetching player data: {response.status_code}")

        player_data = response.json()

        return [Player.from_dict(player['player']) for player in player_data['response']]  

    def get_players_in_team(self):
        url = f"https://v3.football.api-sports.io/players/squads?team={self.team_id}"
        headers = {
        'x-apisports-key': self.api_key,
        'x-rapidapi-host': 'v3.football.api-sports.io'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error fetching player data: {response.status_code}")

        player_data = response.json()
        # team_name = player_data['response'][0]['team']['name']
        # print(f"Team Name: {team_name}")

        return [Player.from_dict(player) for data in player_data['response'] for player in data['players']]
    

    def get_team_details_by_id(self):
        url = f"https://v3.football.api-sports.io/teams?id={self.team_id}"
        headers = {
        'x-apisports-key': self.api_key,
        'x-rapidapi-host': 'v3.football.api-sports.io'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error fetching player data: {response.status_code}")

        team_data = response.json()

        return [Team.from_dict(team['team']) for team in team_data['response']]

    