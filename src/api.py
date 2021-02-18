from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse

from markdown import markdown

from board import Board

app = FastAPI()


def error(exception_name: str, message=None):
    response = {"error": exception_name}

    if message:
        response["error_message"] = message

    return response


@app.get('/', response_class=HTMLResponse)
def home():
    with open("../doc/api_home.md", "r") as fd:
        api_home = fd.read()
        fd.close

    return markdown(api_home)


@app.get("/board/{board_string}/turn/{turn}")
def board(board_string: str, turn: str, response: Response):
    try:
        board = Board(board_string)

    except Board.BoardSizeNotSquareError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return error("Board.BoardSizeNotSquareError",
                     message="Board Size not perfect square.")

    return board.board
