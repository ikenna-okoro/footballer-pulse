import requests
from dotenv import load_dotenv
import os
from domain.player import Player
from domain.team import Team


class FootBallRepository:
    BASE_URL = "https://v3.football.api-sports.io"

    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.headers = {
            'x-apisports-key': self.api_key,
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

    def make_request(self, endpoint: str, params: dict = None):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Error fetching data from External API: {response.status_code}")
        return response.json()

    def get_all_players(self):
        player_data = self.make_request("players/profiles")
        return [Player.from_dict(player['player']) for player in player_data['response']]

    def get_player_by_lastname(self, lastname: str):
        player_data = self.make_request(f"players/profiles", params={"search": lastname})
        return [Player.from_dict(player['player']) for player in player_data['response']]

    def get_player_by_id(self, player_id: int):
        player_data = self.make_request("players/profiles", params={"player": player_id})
        return [Player.from_dict(player['player']) for player in player_data['response']]  

    def get_players_in_team(self, team_id: int):
        player_data = self.make_request("players/squads", params={"team": team_id})
        return [Player.from_dict(player) for data in player_data['response'] for player in data['players']]

    def get_team_details_by_id(self, team_id: str):
        team_data = self.make_request("teams", params={"id": team_id})
        return [Team.from_dict(team['team']) for team in team_data['response']]