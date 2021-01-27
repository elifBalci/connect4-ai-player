import copy
from math import inf
from evaluation import evaluate, winning_move, check_diagonal
from board import Board
from piece import Piece


def minimax(depth, max_player, board, column, evaluation_number):
    board_to_use = copy.deepcopy(board)
    if depth == 0:
        point = evaluate(board_to_use, max_player, evaluation_number)
        return point, column
    if winning_move(board, max_player, evaluation_number):
        return 99999, None

    if max_player == "y":
        best_move = None
        max_res = -inf
        for i in range(board.size[1]):
            piece = Piece(max_player, i, 0)
            child_board = copy.deepcopy(board_to_use)
            if child_board.is_column_full(i):
                continue
            child_board.drop_piece(piece)
            res = minimax(depth - 1, "x", child_board, i, evaluation_number)[0]
            max_res = max(max_res, res)
            if max_res == res:
                best_move = i
        return max_res, best_move

    if max_player == "x":
        best_move = None
        min_res = inf
        for i in range(board.size[1]):
            piece = Piece(max_player, i, 0)
            child_board = copy.deepcopy(board_to_use)
            if child_board.is_column_full(i):
                continue
            child_board.drop_piece(piece)
            res = minimax(depth - 1, "y", child_board, i, evaluation_number)[0]
            min_res = min(min_res, res)
            if min_res == res:
                best_move = i
        return min_res, best_move


def main():
    board_size = (6, 7)
    board = Board(board_size)

    piece = Piece("y", 0, 0)
    board.drop_piece(piece)

    piece = Piece("x", 2, 0)
    board.drop_piece(piece)

    piece = Piece("x", 3, 0)
    board.drop_piece(piece)
    board.drop_piece(piece)
    board.drop_piece(piece)
    piece = Piece("y", 3, 0)
    board.drop_piece(piece)

    piece = Piece("y", 4, 0)
    board.drop_piece(piece)
    board.drop_piece(piece)
    piece = Piece("x", 4, 0)
    board.drop_piece(piece)

    piece = Piece("x", 5, 0)
    board.drop_piece(piece)
    piece = Piece("y", 5, 0)
    board.drop_piece(piece)
    piece = Piece("x", 5, 0)
    board.drop_piece(piece)

    piece = Piece("y", 6, 0)
    board.drop_piece(piece)
    board.drop_piece(piece)

    board.print_board()
    print("winner", board.check_win_2())
    point, best_move = minimax(2, "y", board, -1, 0)
    print("best move for y", best_move)


def play(board, player, tree_depth, evaluation_number):
    point, best_move = minimax(tree_depth, player, board, -1, evaluation_number)
    return best_move


if __name__ == "__main__":
    main()
