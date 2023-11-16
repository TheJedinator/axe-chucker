from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from textual.containers import ScrollableContainer
from textual.widgets import Static, Button
from throwing_entities.game import Game

from throwing_entities.player import Player


class ScoreBoardElement(Static):
    """A score board element"""


class ScoreBoard(Static):
    """Score board"""

    def __init__(self, game: Game | None, **kwargs):
        """Initialize the score board"""
        super().__init__(**kwargs)
        self.game = game

    def compose(self) -> ComposeResult:
        """Compose the score board"""
        yield ScoreBoardElement("Player 1", id="player1_name")

        yield ScoreBoardElement(
            f"Score: {self.game.player1_score if self.game else 0}", id="player1_score"
        )


class CallButtonsContainer(Static):
    """A button container for kill shot calls, fouls, misses and drops"""

    def compose(self) -> ComposeResult:
        """Compose the button container"""
        yield Button("Miss", id="miss_button")
        yield Button("Drop", id="drop_button")
        yield Button("Foul", id="foul_button")
        yield Button("Kill Shot", id="kill_shot_call_button")


class ScoringButtonsContainer(Static):
    """A button container"""

    def compose(self) -> ComposeResult:
        """Compose the button container"""
        yield Button("1", id="score_button1", classes="score_button")
        yield Button("2", id="score_button2", classes="score_button")
        yield Button("3", id="score_button3", classes="score_button")
        yield Button("4", id="score_button4", classes="score_button")
        yield Button("5", id="score_button5", classes="score_button")
        yield Button("6", id="score_button6", classes="score_button")
        yield Button("8", id="score_button8", classes="score_button")


class AxeChucker(App):
    """Axe Chucker App"""

    game = None

    CSS_PATH = "axe_chucker.tcss"
    BINDINGS = [
        ("q", "quit_app", "Quit the app"),
        ("d", "toggle_dark", "Toggle dark mode"),
        ("c", "create_game", "Create a game"),
        ("1", "player1_score", "Player 1 score"),
        ("2", "player2_score", "Player 2 score"),
        ("3", "player1_throws", "Player 1 throws"),
        ("4", "player2_throws", "Player 2 throws"),
    ]

    async def on_mount(self, event):
        """On mount, create a game"""
        await self.create_game()

    async def create_game(self):
        """Create a game"""
        self.game = Game(
            player1=Player(name="Player 1"),
            player2=Player(name="Player 2"),
            player1_score=0,
            player2_score=0,
            player1_throws=0,
            player2_throws=0,
        )

    def compose(self):
        """Compose the app"""
        yield Header()
        yield Footer()
        yield ScrollableContainer(
            ScoreBoard(game=self.game),
            ScoringButtonsContainer(),
            CallButtonsContainer(),
        )

    async def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    async def action_quit_app(self) -> None:
        """Quit the app."""
        self.exit()

    async def action_create_game(self) -> None:
        """Create a game."""
        await self.create_game()


if __name__ == "__main__":
    app = AxeChucker()
    app.run()
