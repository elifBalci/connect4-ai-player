import minimax
from board import Board
from piece import Piece
import time


class Main:
    board_size = (6, 7)

    def __init__(self):
        self.board = None
        self.create_puzzle_and_solver()

    def create_puzzle_and_solver(self):
        self.board = Board(self.board_size)


def main():
    val = int(input("Choose game mode\n 1 - human vs human\n 2 - human vs AI\n 3 - AI vs AI\t"))
    if val == 1:
        human_vs_human()
    if val == 2:
        depth = int(input("Choose depth of tree (4 recommended)"))
        ev = int(input("Choose evaluation function number (0, 1, 2)"))
        human_vs_ai(depth, ev)
    if val == 3:
        depth1 = int(input("Choose depth of tree for player X (Below 5 recommended)"))
        depth2 = int(input("Choose depth of tree for player Y (Below 5 recommended)"))
        ev1 = int(input("Choose evaluation function number (0, 1, 2)"))
        ev2 = int(input("Choose evaluation function number (0, 1, 2)"))
        ai_vs_ai(depth1, depth2, ev1, ev2)


def human_vs_human():
    starter = Main()
    starter.board.print_board()
    player = "x"
    while True:
        val = input("Player " + str(player) + " please enter column number: ")
        print(val)
        play_round(player, int(val), starter)
        if player == "x":
            player = "y"
        else:
            player = "x"


def human_vs_ai(depth, ev):
    starter = Main()
    starter.board.print_board()
    player = "x"
    while True:
        val = input("Player " + str(player) + " please enter column number: ")
        action = int(val)
        play_round(player, action, starter)
        action = minimax.play(starter.board, "y", depth, ev)
        play_round("y", action, starter)


def ai_vs_ai(depth1, depth2, ev1, ev2):
    starter = Main()
    starter.board.print_board()
    while True:
        action = minimax.play(starter.board, "x", depth1, ev1)
        play_round("x", action, starter)

        action = minimax.play(starter.board, "y", depth2, ev2)
        play_round("y", action, starter)


def play_round(player, action, starter):
    if not 0 <= action < starter.board.size[1]:
        print("Input is not appropriate")
        return
    piece = Piece(player, action, 0)
    if starter.board.is_column_full(action):
        print("Selected row is full!")
        return
    starter.board.drop_piece(piece)
    starter.board.print_board()
    check_win(starter.board)
    time.sleep(0.5)


def check_win(board):
    winner = board.check_win_2()
    if winner is not None:
        print("Player " + str(winner) + " win the game!!")
        exit(0)


if __name__ == '__main__':
    main()
