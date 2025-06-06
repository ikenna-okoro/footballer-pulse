import dataclasses
from typing import Optional

@dataclasses.dataclass
class Team:
    id: int
    name: str
    code: str
    country: str
    founded: int
    national: bool
    logo: str


    @classmethod
    def from_dict(cls, d):
        return cls(**d)
    

    def to_dict(self):
        return dataclasses.asdict(self)