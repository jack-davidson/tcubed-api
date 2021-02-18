from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse, JSONResponse

from markdown import markdown

from board import Board, BoardSizeNotSquareError, players

from error import error

api = FastAPI()


@api.get('/')
def home():
    with open("../doc/api_home.md", "r") as fd:
        api_home = fd.read()
        fd.close

    return HTMLResponse(markdown(api_home))


# receives board encoded as string and turn
# returns coordinates of best move
@api.get("/board/{board_string}/turn/{turn}", response_class=JSONResponse)
def board(board_string: str, turn: str, response: Response):
    try:
        board = Board(len(board_string), players[turn])
    except BoardSizeNotSquareError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return error("BoardSizeNotSquareError",
                     "Board Size not perfect square."),

    return board.eval()
