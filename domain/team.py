import dataclasses
from typing import Optional

@dataclasses.dataclass
class Team:
    id: int
    name: str
    code: Optional[str] = None
    country: Optional[str] = None
    founded: Optional[int] = None
    national: Optional[bool] = None
    logo: Optional[str] = None


    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)