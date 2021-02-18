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


# Board size is not perfect square.
class BoardSizeNotSquareError(Exception):
    pass


class Board:
    def __init__(self, size: int, turn: int):
        if not perfect_square(size):
            raise BoardSizeNotSquareError

        # 'Allocate' a square board.
        self.board = [[players['E']] * int_sqrt(size)] * int_sqrt(size)

        self.turn = turn

    # TODO
    def set_board():
        pass

    # TODO
    # Return board with best move.
    def best_move(self) -> str:
        return self.board

    # Check if empty spots still in board.
    def moves_left(self) -> bool:
        for row in self.board:
            for spot in row:
                if spot == players['E']:
                    return True
        return False

    # TODO
    # Use minimax to solve board.
    def minimax(self, depth=0) -> int:
        pass

    # TODO
    # Evaluate score of board.
    def eval(self) -> int:

        # Check rows for win.
        for row in self.board:
            if sum(row) == players[config.MAXIMIZER] * len(row):
                return 10
            elif sum(row) == players[config.MINIMIZER] * len(row):
                return -10
