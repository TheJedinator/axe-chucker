from uuid import UUID, uuid4
from dataclasses import dataclass


@dataclass(frozen=True)
class Throw:
    game_id: UUID
    player_id: UUID
    id: UUID = uuid4()
    score: int = 0
    kill_shot: bool = False
    drop: bool = False
    miss: bool = False
    fault: bool = False
