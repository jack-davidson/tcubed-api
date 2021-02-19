from fastapi import FastAPI, Response

from fastapi.responses import HTMLResponse, JSONResponse

from fastapi.middleware.cors import CORSMiddleware

from markdown import markdown

from board import board_string_to_matrix, board_matrix_to_string

from player import Player

api = FastAPI()

origins = [
    "http://0.0.0.0:8000",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# home route renders markdown homepage
@api.get('/', response_class=HTMLResponse)
def home():
    with open("../doc/api_home.md", "r") as fd:
        api_home = fd.read()
        fd.close

    return markdown(api_home)


# receives board encoded as string and turn
# returns coordinates of best move
@api.get("/board/{board_string}/player/{player}", response_class=JSONResponse)
def board(board_string: str, player: str, response: Response):
    return board_string_to_matrix(board_string)


@api.get("/test/board_matrix_to_string")
def test_board_matrix_to_string():
    return board_matrix_to_string([[Player.E] * 3] * 3)
