from error_response import ErrorResponse, err
import config


class Errors(ErrorResponse):
    def invalid_player_error():
        return err("BoardSizeNotSquareError",
                   "Board Size not square.")

    def board_size_not_square_error():
        return err("InvalidPlayerError",
                   f"Player is not {config.maximizer} "
                   f"or {config.minimizer}.")
