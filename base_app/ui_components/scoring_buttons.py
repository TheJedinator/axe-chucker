from textual.widgets import Static, Button
from textual.app import ComposeResult


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
