from evaluation import check_diagonal, evaluate, max_in_row_col


class Board:
    def __init__(self, size):
        self.size = size
        self.board = None
        self.create_board()

    def create_board(self):
        self.board = [["_" for i in range(self.size[1])] for j in range(self.size[0])]

    def print_board(self):
        print("  0 1 2 3 4 5 6")
        for i in range(self.size[0]):
            print(i, end=" ")
            for j in range(self.size[1]):
                print(self.board[i][j], end=" ")
            print()

    def drop_piece(self, piece):
        column = piece.location
        player = piece.player
        last_empty = self.last_empty(column)
        piece.row = last_empty
        self.board[last_empty][column] = player

    def retrieve_piece(self, piece):
        column = piece.location
        last_empty = self.last_empty(column)
        self.board[last_empty + 1][column] = "_"
        print()
        self.print_board()

    def last_empty(self, column):
        for i in range(self.size[0]):
            if self.board[self.size[0] - i - 1][column] == "_":
                return self.size[0] - i - 1

    def is_column_full(self, column):
        if self.board[0][column] != "_":
            return True
        else:
            return False

    def check_win(self):
        player = "x"
        player2 = "y"

        consecutive_p1 = 0
        consecutive_p2 = 0
        max_consecutive_column_p1 = 0
        max_consecutive_column_p2 = 0
        # column consecutive check
        for j in range(7):
            for i in range(6):
                if self.board[i][j] == player:
                    consecutive_p1 = consecutive_p1 + 1
                    max_consecutive_column_p1 = max(consecutive_p1, max_consecutive_column_p1)
                if self.board[i][j] == player2:
                    consecutive_p2 = consecutive_p2 + 1
                    max_consecutive_column_p2 = max(consecutive_p2, max_consecutive_column_p2)
                elif self.board[i][j] == "_":
                    consecutive_p1 = 0
                    consecutive_p2 = 0
                    max_consecutive_column_p1 = max(consecutive_p1, max_consecutive_column_p1)
                    max_consecutive_column_p2 = max(consecutive_p2, max_consecutive_column_p2)

        # row consecutive check
        consecutive_p1 = 0
        consecutive_p2 = 0
        max_consecutive_row_p1 = 0
        max_consecutive_row_p2 = 0
        for i in range(6):
            for j in range(7):
                if self.board[i][j] == player:
                    consecutive_p1 = consecutive_p1 + 1
                    max_consecutive_row_p1 = max(consecutive_p1, max_consecutive_row_p1)
                if self.board[i][j] == player2:
                    consecutive_p2 = consecutive_p2 + 1
                    max_consecutive_row_p2 = max(consecutive_p2, max_consecutive_row_p2)
                elif self.board[i][j] == "_":
                    consecutive_p1 = 0
                    consecutive_p2 = 0
                    max_consecutive_row_p2 = max(consecutive_p2, max_consecutive_row_p2)
                    max_consecutive_row_p1 = max(consecutive_p1, max_consecutive_row_p1)

        if max_consecutive_column_p1 >= 4 or max_consecutive_row_p1 >= 4:
            return player
        elif max_consecutive_column_p2 >= 4 or max_consecutive_row_p2 >= 4:
            return player2
        max_diag = check_diagonal(self.board, player)[1]
        if max_diag >= 4:
            return player
        max_diag = check_diagonal(self.board, player2)[1]
        if max_diag >= 4:
            return player2

        return None

    def check_win_2(self):
        max_x = max_in_row_col("x", self.board)
        max_y = max_in_row_col("y", self.board)
        if max_x >= 4:
            return "x"
        elif max_y >= 4:
            return "y"

        l, max_diag_x, max_diag_x_cw = check_diagonal(self.board, "x")
        if max_diag_x >= 4 or max_diag_x_cw >= 4:
            return "x"
        l, max_diag_y, max_diag_y_cw = check_diagonal(self.board, "y")
        if max_diag_y >= 4 or max_diag_y_cw >= 4:
            return "y"
        return None
