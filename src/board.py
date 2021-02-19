from square import int_sqrt, perfect_square
import config

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


def convert_board_string(board_string: str):
    board = []
    for i in range(9):
        if i % 3 == 0:
            board.append([i for i in board_string[i:i+3]])
    return board
