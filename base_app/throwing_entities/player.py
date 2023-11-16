from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Player:
    name: str
    id: UUID = uuid4()
