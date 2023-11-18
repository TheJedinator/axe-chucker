from textual.widgets import Static, Button
from textual.app import ComposeResult


class CallButtonsContainer(Static):
    """A button container for kill shot calls, fouls, misses and drops"""

    def compose(self) -> ComposeResult:
        """Compose the button container"""
        yield Button("Miss", id="miss_button")
        yield Button("Drop", id="drop_button")
        yield Button("Foul", id="foul_button")
        yield Button("Kill Shot", id="kill_shot_call_button")
