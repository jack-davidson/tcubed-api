from fastapi import FastAPI, Response, status

from fastapi.responses import HTMLResponse, JSONResponse

from markdown import markdown

from board import Board
from board import players
from board import BoardSizeNotSquareError, InvalidPlayerError

from error import error

import config

api = FastAPI()


@api.get('/')
def home():
    with open("../doc/api_home.md", "r") as fd:
        api_home = fd.read()
        fd.close

    return HTMLResponse(markdown(api_home))


# receives board encoded as string and turn
# returns coordinates of best move
@api.get("/board/{board_string}/player/{player}", response_class=JSONResponse)
def board(board_string: str, player: str, response: Response):
    try:
        board = Board(len(board_string), players[player])

    except KeyError:
        if player is not config.maximizer or config.minimizer:
            return error("InvalidPlayerError",
                         f"Player is not {config.maximizer}"
                         "or {config.minimizer}.")

    except BoardSizeNotSquareError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return error("BoardSizeNotSquareError",
                     "Board Size not square.")

    except InvalidPlayerError:
        return error("InvalidPlayerError", f"Player is not {config.maximizer}"
                     "or {config.minimizer}.")

    return board.board
