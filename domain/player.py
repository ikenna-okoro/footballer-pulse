import dataclasses

@dataclasses.dataclass
class Player:
    id: int
    name: str
    firstname: str
    age: int
    birth: str
    height: str
    weight: str
    photo: str
    lastname: str
    position: str
    number: int
    nationality: str


    @classmethod
    def from_dict(cls, d):
        return cls(**d)
    

    def to_dict(self):
        return dataclasses.asdict(self)