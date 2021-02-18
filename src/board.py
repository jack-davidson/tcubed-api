from square import int_sqrt, perfect_square
import config

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
    def __init__(self, board_string: str):
        size = len(board_string)
        if not perfect_square(size):
            raise BoardSizeNotSquareError

        # 'Allocate' a square board.
        self.board = [[players['E']] * int_sqrt(size)] * int_sqrt(size)
        self.turn = players[config.DEFAULT_TURN]

        # set board from board_string

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

    # Use minimax to solve board.
    def minimax(self, depth: int) -> int:
        pass

    # Evaluate score of board.
    def eval(self) -> int:
        pass
