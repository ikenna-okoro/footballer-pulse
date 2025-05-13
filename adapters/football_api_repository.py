import requests
from entities.player import Player
from interactors.get_player_details import PlayerRepository


class FootballAPIPlayerRepository(PlayerRepository):
    
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_player_by_id(self, player_id: int) -> Player:
        url = f"https://v3.football.api-sports.io/players/profiles?player={player_id}"
        headers = {
        'x-apisports-key': self.api_key,
        'x-rapidapi-host': 'v3.football.api-sports.io'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            player_data = response.json()
            player = Player(
                id=player_data['response'][0]['player']['id'],
                name=player_data['response'][0]['player']['name'],
                position=player_data['response'][0]['player']['position'],
                nationality=player_data['response'][0]['player']['nationality']
            )
            return player.__repr__()
            # return {
            #     "id": player.id,
            #     "name": player.name,
            #     "position": player.position,
            #     "nationality": player.nationality
            # }
        
        else:
            raise Exception(f"Error fetching player data: {response.status_code}")
        



