import dataclasses
from typing import Optional

@dataclasses.dataclass
class Player:
    id: int
    name: str
    age: int
    photo: str
    position: str
    number: int
    firstname: Optional[str] = ""
    birth: Optional[str] = ""
    height: Optional[str] = ""
    weight: Optional[str] = ""
    lastname: Optional[str] = ""
    nationality: Optional[str] = ""


    @classmethod
    def from_dict(cls, d):
        return cls(**d)
    

    def to_dict(self):
        return dataclasses.asdict(self)