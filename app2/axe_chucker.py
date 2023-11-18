import tkinter as tk


class Game:
    def __init__(self, player1: str, player2: str):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.player1_throws = []
        self.player2_throws = []


class Player:
    def __init__(self, name: str):
        self.name = name
        self.throws = []


class Throw:
    def __init__(
        self,
        game_id: int,
        player_id: int,
        score: int,
        kill_shot: bool = False,
        fault: bool = False,
        drop: bool = False,
        miss: bool = False,
    ):
        self.game_id = game_id
        self.player_id = player_id
        self.score = score
        self.kill_shot = kill_shot
        self.fault = fault
        self.drop = drop
        self.miss = miss

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score


def create_name_input():
    player1_name = tk.StringVar()
    player2_name = tk.StringVar()
    player1_name_entry = tk.Entry(root, textvariable=player1_name)
    player2_name_entry = tk.Entry(root, textvariable=player2_name)
    player1_name_entry.grid(row=0, column=0)
    player2_name_entry.grid(row=0, column=1)
    submit_button = tk.Button(
        root,
        text="Submit",
        command=lambda: (
            start_game(player1_name.get(), player2_name.get()),
            player1_name_entry.grid_remove(),
            player2_name_entry.grid_remove(),
            submit_button.grid_remove(),
        ),
    )
    submit_button.grid(row=1, column=0, columnspan=2)


def start_game(player1_name: str, player2_name: str):
    game = Game(player1_name, player2_name)
    player1_score = create_scoreboard(game.player1, 2, 0)
    player2_score = create_scoreboard(game.player2, 2, 2)
    create_score_buttons(game.player1, 0)
    create_score_buttons(game.player2, 2)
    create_call_buttons(game.player1, 10)
    create_call_buttons(game.player2, 11)


def create_scoreboard(player, row, column):
    player_name = tk.Label(root, text=player.name)
    player_name.grid(row=row, column=column, columnspan=2)
    player_score = tk.StringVar()
    player_score.set(str(sum([throw.get_score() for throw in player.throws])))
    player_scoreboard = tk.Label(root, textvariable=player_score)
    player_scoreboard.grid(row=row + 1, column=column, columnspan=2)
    return player_score


def create_score_buttons(player: Player, column_start):
    scores = [[1, 2, 3], [4, 5, 6], [8]]
    for row, score_row in enumerate(scores):
        for column, score in enumerate(score_row):
            color = "black"
            if score == 8:
                color = "blue"
            tk.Button(
                root,
                text=str(score),
                command=lambda score=score: (
                    player.throws.append(Throw(game_id=1, player_id=1, score=score)),
                    player1_score.set(
                        str(sum([throw.get_score() for throw in game.player1.throws]))
                    ),
                    player2_score.set(
                        str(sum([throw.get_score() for throw in game.player2.throws]))
                    ),
                ),
                fg=color,
            ).grid(row=row + 2, column=column + column_start, columnspan=2)


def create_call_buttons(player: Player, row_start):
    for i, call in enumerate(["Kill Shot", "Miss", "Drop", "Fault", "Zero"]):
        tk.Button(
            root,
            text=call,
            command=lambda call=call: (
                player.throws.append(
                    Throw(
                        game_id=1,
                        player_id=1,
                        score=(0 if call in ["Miss", "Drop", "Fault", "Zero"] else 8),
                    )
                ),
                player1_score.set(
                    str(sum([throw.get_score() for throw in game.player1.throws]))
                ),
                player2_score.set(
                    str(sum([throw.get_score() for throw in game.player2.throws]))
                ),
            ),
        ).grid(row=row_start, column=i, columnspan=2)


root = tk.Tk()
root.geometry("1920x1080")
create_name_input()
root.mainloop()
