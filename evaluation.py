def evaluate(board, player, evaluation_number):
    player_points = give_point_to_player(board, player, evaluation_number)
    if player == "x":
        opponent = "y"
    else:
        opponent = "x"
    opponent_points = give_point_to_player(board, opponent, evaluation_number)
    points = player_points - opponent_points
    if opponent == "y":
        points = points * -1

    return points


def give_point_to_player(board, player, evaluation_number):
    consecutive = 0
    max_consecutive_column = 0
    middle = 0
    for i in range(6):
        for j in range(7):
            if j == 3 and board.board[i][j] == player:
                middle = middle + 1

    # column consecutive check
    for j in range(7):
        for i in range(6):
            if board.board[i][j] == player:
                consecutive = consecutive + 1
                max_consecutive_column = max(consecutive, max_consecutive_column)
            else:
                consecutive = 0
                max_consecutive_column = max(consecutive, max_consecutive_column)

    # row consecutive check
    consecutive = 0
    max_consecutive_row = 0
    for i in range(6):
        for j in range(7):
            if board.board[i][j] == player:
                consecutive = consecutive + 1
                max_consecutive_row = max(consecutive, max_consecutive_row)
            else:
                consecutive = 0
                max_consecutive_row = max(consecutive, max_consecutive_row)

    diagonal_list = check_diagonal(board.board, player)[0]
    points = 0
    if evaluation_number == 0:
        points = give_points_evaluation_1(max_consecutive_column, max_consecutive_row, middle, diagonal_list)
    if evaluation_number == 1:
        points = give_points_evaluation_2(max_consecutive_column, max_consecutive_row, diagonal_list)
    if evaluation_number == 2:
        points = give_points_evaluation_3(max_consecutive_column, max_consecutive_row, middle, diagonal_list)
    return points


def give_points_evaluation_1(max_col, max_row, middle, diagonal_list):
    points = 0
    if max_col == 3:
        points = points + 80
    if max_col == 2:
        points = points + 30

    if max_row == 3:
        points = points + 80
    if max_row == 2:
        points = points + 30

    for i in diagonal_list:
        if i == 2:
            points = points + 15
        if i == 3:
            points = points + 40
        if i >= 4:
            points = points + 99999

    points = middle + points
    if max_col >= 4 or max_row >= 4:
        points = points + 99999
    return points


def give_points_evaluation_2(max_col, max_row, diagonal_list):
    points = 0
    if max_col == 3:
        points = points + 100
    if max_col == 2:
        points = points + 30

    if max_row == 3:
        points = points + 100
    if max_row == 2:
        points = points + 30

    for i in diagonal_list:
        if i == 2:
            points = points + 30
        if i == 3:
            points = points + 80
        if i >= 4:
            points = points + 99999

    if max_col >= 4 or max_row >= 4:
        points = points + 99999
    return points


def give_points_evaluation_3(max_col, max_row, middle, diagonal_list):
    points = middle * 5
    if max_col == 3:
        points = points + 100
    if max_col == 2:
        points = points + 50

    if max_row == 3:
        points = points + 100
    if max_row == 2:
        points = points + 50

    for i in diagonal_list:
        if i == 2:
            points = points + 50
        if i == 3:
            points = points + 150
        if i >= 4:
            points = points + 99999

    if max_col >= 4 or max_row >= 4:
        points = points + 99999
    return points


def winning_move(board, player, evaluation_number):
    if evaluate(board, player, evaluation_number) >= 99999:
        return True


def check_diagonal(board, player):
    max_col = len(board[0])
    max_row = len(board)
    column = [[] for _ in range(max_col)]
    row = [[] for _ in range(max_row)]
    diagonal_1st_dir = [[] for _ in range(max_row + max_col - 1)]
    diagonal_2nd_dir = [[] for _ in range(len(diagonal_1st_dir))]
    min_diag_cons = -max_row + 1
    for i in range(max_col):
        for j in range(max_row):
            column[i].append(board[j][i])
            row[j].append(board[j][i])
            diagonal_1st_dir[i + j].append(board[j][i])
            diagonal_2nd_dir[i - j - min_diag_cons].append(board[j][i])
    p1 = process_diagonal(diagonal_1st_dir, player)
    p2 = process_diagonal(diagonal_2nd_dir, player)
    list_diagonals = p1[0] + p2[0]
    return list_diagonals, p1[1], p2[1]


def process_diagonal(diagonal_list, player):
    max_consecutive = 0
    max_for_element = 0
    consecutive = 0
    list_of_consecutive = []
    for list_element in diagonal_list:
        for element in list_element:
            for e in element:
                if e == player:
                    consecutive = consecutive + 1
                    max_consecutive = max(max_consecutive, consecutive)
                else:
                    consecutive = 0
        consecutive = 0
        if max_consecutive != 0:
            list_of_consecutive.append(max_consecutive)
        max_for_element = max(max_consecutive, max_for_element)
        max_consecutive = 0
    if list_of_consecutive:
        max_for_element = max(list_of_consecutive)
    return list_of_consecutive, max_for_element


def max_in_row_col(player, board):
    max_col = 7
    max_row = 6
    column = [[] for _ in range(max_col)]
    row = [[] for _ in range(max_row)]
    for x in range(max_col):
        for y in range(max_row):
            column[x].append(board[y][x])
            row[y].append(board[y][x])
    max_consecutive = 0
    max_for_element = 0
    consecutive = 0
    for list_element in column:
        for element in list_element:
            if element == player:
                consecutive = consecutive + 1
                max_consecutive = max(max_consecutive, consecutive)
            else:
                consecutive = 0
        consecutive = 0
        max_for_element = max(max_consecutive, max_for_element)
        max_consecutive = 0

    max_consecutive = 0
    consecutive = 0
    for list_element in row:
        for element in list_element:
            if element == player:
                consecutive = consecutive + 1
                max_consecutive = max(max_consecutive, consecutive)
            else:
                consecutive = 0
        consecutive = 0
        max_for_element = max(max_consecutive, max_for_element)
        max_consecutive = 0
    return max_for_element
