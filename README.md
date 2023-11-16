# Axe Chucker - Game

An axe throwing score keeper and game manager. Written in Python. Intended to track scoring in a World Axe Throwing League (WATL) game.

### General Axe Throwing Rules:
- A game consists of 10 throws per player. 5 per side.
- A lane consists of 2 targets. 1 per side.
- A player throws 5 times on one side and 5 times on the other side.
- The player with the most points wins.
- Each throw is scored based on the number of points the axe is touching.
- Scoring is 1 through 6 points. And a kill shot for 8 points.
- A kill shot must be called before the throw.
- A fault (stepping over the foul line) is a 0
- A drop is a 0
- Hitting the target outside the throwing area is 0
- Calling a kill shot and missing is considered a miss and results in 0 points
- A player can call a maximum of 2 kill shots per game except in the event of a drop which allows for a 3rd kill shot, but must be thrown with in the regulation 10 throws. 
- In the event of a tie there is a sudden death kill shot. The player closest to the kill shot wins. Play continues until there is a winner.

## Application Requirements
- Record the score of each throw
- Record the score of each player
- Record the score of each game
- Allow for a kill shot to be called
- Record all scores in range 0 - 6 and 8
- Record a fault
- Record a drop
- Record a kill shot
- Record a miss
- Record a sudden death kill shot
- Announce the winner
- Keep score visible
- Indicate when to switch sides
- Only allow for 2 kill shots per game
- Allow for a 3rd kill shot in the event of a drop recorded previously
- Only allow for 10 throws per game
- Indicate when a player has thrown 5 times on one side
- Visually indicate which throws have been recorded
- Visually indicate which side the player is throwing on


## Data Model
### Game
- `id` - unique identifier for the game
- `player1` - player 1
- `player2` - player 2
- `player1_score` - player 1 cumulative score
- `player2_score` - player 2 cumulative score
- `player1_throws` - list of player 1 throws
- `player2_throws` - list of player 2 throws

### Player
- `id` - unique identifier for the player
- `name` - name of the player

### Throw
- `id` - unique identifier for the throw
- `game_id` - unique identifier for the game
- `player_id` - unique identifier for the player
- `score` - score of the throw
- `kill_shot` - boolean indicating if the throw was a kill shot
- `fault` - boolean indicating if the throw was a fault
- `drop` - boolean indicating if the throw was a drop
- `miss` - boolean indicating if the throw was a miss

## Architecture
Phase 1 - In Memory
Phase 2 - Database?
Phase 3 - Alternative UI


## UI
Tkinter

## To Play
