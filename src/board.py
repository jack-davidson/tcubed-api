from player import Player
from math import sqrt


# player lookup
players = {
    'E': Player.E,  # E: Empty
    'X': Player.X,  # X: player 'X'
    'O': Player.O,  # O: player 'O'
}


# reverse player lookup
reverse_players = {
    value: key for (key, value) in players.items()
}


def board_string_to_matrix(board_string: str) -> list[Player]:
    board = []
    length = len(board_string)

    for i in range(length):
        if not i % int(sqrt(length)):
            board.append([i for i in list(map(lambda c: players[c],
                                              list(board_string)))[i:i+3]])

    return board


def board_matrix_to_string(board_matrix: list[Player]) -> str:
    board_string = ""
    for row in board_matrix:
        for player in row:
            board_string += reverse_players[player]

    return board_string


def moves_left(board_matrix: list[Player]) -> bool:
    for row in board_matrix:
        for cell in row:
            if cell == Player.E:
                return True

    return False


def eval_board(board_matrix: list[Player]) -> int:
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
