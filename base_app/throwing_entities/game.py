from dataclasses import dataclass
from uuid import UUID, uuid4

from .player import Player


@dataclass()
class Game:
    player1: Player
    player2: Player
    player1_score: int
    player2_score: int
    player1_throws: int
    player2_throws: int
    id: UUID = uuid4()

    def __str__(self):
        return f"{self.player1.name} vs {self.player2.name}"

    def set_player1_score(self, score: int):
        self.player1_score = score

    def set_player2_score(self, score: int):
        self.player2_score = score

    def set_player1_throws(self, throws: int):
        self.player1_throws = throws

    def set_player2_throws(self, throws: int):
        self.player2_throws = throws
