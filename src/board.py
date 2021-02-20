from player import Player, players, reverse_players
from math import sqrt


# Deserialize a board.
def board_string_to_matrix(board_string: str) -> list[Player]:
    board = []
    length = len(board_string)

    # This is not hard coded and works for any size board.
    for i in range(length):
        if not i % int(sqrt(length)):
            # Map (c) => players[c] to board_string and take slice of one row.
            row = list(map(lambda c: players[c],
                           list(board_string)))[i:i + int(sqrt(length))]
            board.append([x for x in row])  # append each element in row

    return board


# Serialize a board.
def board_matrix_to_string(board_matrix: list[list[Player]]) -> str:
    board_string = ""
    for row in board_matrix:
        for cell in row:
            board_string += reverse_players[cell]

    return board_string


# Search board for empty cells, if there are any, there are moves left and
# return True.
def moves_left(board_matrix: list[list[Player]]) -> bool:
    for row in board_matrix:
        for cell in row:
            if cell == Player.E:
                return True

    return False


# Evaluate board and return a score.
# This is a naïve solution and only works with 3x3 boards.
def eval_board(board_matrix: list[list[Player]]) -> int:
    for row in range(0, 3):
        if board_matrix[row][0] == board_matrix[row][1] and board_matrix[row][1] == board_matrix[row][2]:
            if board_matrix[row][0] == Player.X:
                return 10
            elif board_matrix[row][0] == Player.O:
                return -10

    for col in range(0, 3):
        if board_matrix[0][col] == board_matrix[1][col] and board_matrix[1][col] == board_matrix[2][col]:
            if board_matrix[0][col] == 'x':
                return 10
            elif board_matrix[0][col] == 'o':
                return -10

    if board_matrix[0][0] == board_matrix[1][1] and board_matrix[1][1] == board_matrix[2][2]:
        if board_matrix[0][0] == 'x':
            return 10
        elif board_matrix[0][0] == 'o':
            return -10

    if board_matrix[0][2] == board_matrix[1][1] and board_matrix[1][1] == board_matrix[2][0]:
        if board_matrix[0][2] == 'x':
            return 10
        elif board_matrix[0][2] == 'o':
            return -10

    return 0


# minimax algorithm
# must be reimplemented for use with arbitrarily sized boards
def minimax(board_matrix: list[list[Player]], depth: int, player: Player) -> int:
    score = eval_board(board_matrix)

    if score == 10 or -10:
        return score

    if not moves_left(board_matrix):
        return 0

    if player == Player.X:
        best = -1000

        for i in range(3):
            for j in range(3):
                if board_matrix[i][j] == Player.E:
                    board_matrix[i][j] = player
                    best = max(best, minimax(board_matrix,
                                             depth + 1,
                                             Player.toggle(player)))
                    board_matrix[i][j] = Player.E
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board_matrix[i][j] == Player.E:
                    board_matrix[i][j] = Player.toggle(player)
                    best = min(best, minimax(board_matrix,
                                             depth + 1,
                                             Player.toggle(player)))
        return best


def find_best_move(board_matrix: list[list[Player]], player: Player) -> tuple[int]:
    best_score = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board_matrix[i][j] == Player.E:
                board_matrix[i][j] = player
                score = minimax(board_matrix, 0, player)
                board_matrix[i][j] = Player.E
                if score > best_score:
                    best_move = (i, j)
                    best_score = score

    return best_move
