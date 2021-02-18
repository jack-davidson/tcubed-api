from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse

from markdown import markdown

from board import Board, BoardSizeNotSquareError

api = FastAPI()


def error(exception_name: str, message=None):
    response = {"error": exception_name}

    if message:
        response["error_message"] = message

    return response


@api.get('/', response_class=HTMLResponse)
def home():
    with open("../doc/api_home.md", "r") as fd:
        api_home = fd.read()
        fd.close

    return markdown(api_home)


@api.get("/board/{board_string}/turn/{turn}")
def board(board_string: str, turn: str, response: Response):
    try:
        board = Board(board_string)

    except BoardSizeNotSquareError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return error("BoardSizeNotSquareError",
                     message="Board Size not perfect square.")

    return board.board
