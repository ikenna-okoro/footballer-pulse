class Player:
    def __init__(self, id: int, name: str, position: str, nationality: str):
        self.id = id
        self.name = name
        self.position = position
        self.nationality = nationality

    def __str__(self):
        return f"{self.name} ({self.position} - {self.nationality})"
        

