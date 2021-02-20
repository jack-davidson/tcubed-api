from math import sqrt
from player import Player


def moves_left(board: list[list[Player]]) -> bool:
    for row in board:
        for cell in row:
            if cell == Player.E:
                return True
    return False


def evaluate(board: list[list[Player]], player: Player) -> bool:
    # Checking for Rows for X or O victory.
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == player:
                return 10

            elif board[row][0] == -player:
                return -10

    # Checking for Columns for X or O victory.
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == player:
                return 10

            elif board[0][col] == -player:
                return -10

    # Checking for Diagonals for X or O victory.
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == player:
            return 10

        elif board[0][0] == -player:
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == player:
            return 10

        elif board[0][2] == -player:
            return -10

    # Else if none of them have won then return 0
    return 0


def minimax(board: list[list[Player]], depth: int, is_max: bool, player: Player):
    score = evaluate(board, player)
    if score == 10:
        return score

    if score == -10:
        return score

    if not moves_left(board):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == Player.E:
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not is_max,
                                             player))
                    board[i][j] = Player.E

        return best

    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == Player.E:
                    board[i][j] = -player
                    best = min(best, minimax(board, depth + 1, not is_max,
                                             player))
                    board[i][j] = Player.E

        return best


def best_move(board, player):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == Player.E:
                board[i][j] = player
                move_val = minimax(board, 0, False, player)
                board[i][j] = Player.E
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    print(best_move)
    return best_move


def deserialize_board(board: str) -> list[list[Player]]:
    return [
        [Player.player(x) for x in board[i:i + int(sqrt(len(board)))]]
        for i in range(0, len(board), int(sqrt(len(board))))]
