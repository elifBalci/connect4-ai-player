# connect4-ai-player

Connect4 game and AI player with text based user interface.
Three game modes are implemented: human vs human, AI vs human and AI vs AI
Minimax algorithm with 3 different evaulation methods are used for the AI player.


**Evaluation-1**

In the first evaluation method the player gained 80 points for every 3 consecutive pieces and 30
points for every 2 consecutive pieces on row, column and diagonal lines. If there are 4
consecutive pieces in any direction the player earns 9999 points. Also the player earns 1 point for
every piece in the middle of the board to motivate players to keep the game in the middle
section. For aggressive defense, opponents points are calculated and subtracted from player’s
points.

**Evaluation-2**

In this evaluation method the player gained 100 points for every 3 consecutive pieces and 30
points for every 2 consecutive pieces on row and column. If there are 4 consecutive pieces in any
direction the player earns 9999 points. Player earns 80 points for every 3 consecutive and 30 for
every 2 consecutive pieces in diagonals which makes AI motivated to connect 4 pieces in vertical
or horizontal lines. Player doesn’t gain any points for pieces in the middle column. For aggressive
defense, opponents points are calculated and subtracted from player’s points.

**Evaluation-3**

In this evaluation method the player gained 100 points for every 3 consecutive pieces and 50
points for every 2 consecutive pieces on row and column. If there are 4 consecutive pieces in any
direction the player earns 9999 points. Player earns 150 points for every 3 consecutive and 50
for every 2 consecutive pieces in diagonals which makes AI motivated to connect 4 pieces in
diagonal which is harder for human player to check. Players gain 5 points for each piece in the
middle column. For aggressive defense, opponents points are calculated and subtracted from
player’s points.
