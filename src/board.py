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


def board_string_to_matrix(board_string: str):
    board_list = []

    for spot in board_string:
        board_list.append(players[spot])

    board = []
    for i in range(9):
        if i % 3 == 0:
            board.append([i for i in board_list[i:i+3]])
    return board
