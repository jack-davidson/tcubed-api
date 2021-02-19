from player import Player
from math import sqrt

# TODO:
# [ ] set_board()
# [ ] eval()
# [ ] minimax()

# player lookup
players = {
    'E': 0,  # E: Empty
    'X': 1,  # X: player 'X'
    'O': 2,  # O: player 'O'
}

# reverse player lookup
reverse_players = {
    0: 'E',
    1: 'X',
    2: 'O',
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
