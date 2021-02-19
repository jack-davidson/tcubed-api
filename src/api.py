from fastapi import FastAPI, Response, status

from fastapi.responses import HTMLResponse, JSONResponse

from markdown import markdown

from board import Board
from board import players
from board import BoardSizeNotSquareError

from errors import Errors

import config

api = FastAPI()


# home route renders markdown homepage
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
    if player != config.maximizer:
        if player != config.minimizer:
            return Errors.invalid_player_error()

    try:
        board = Board(len(board_string), players[player])

    except BoardSizeNotSquareError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return Errors.board_size_not_square_error()

    return board.board
