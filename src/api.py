from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from markdown import markdown

from board import find_best_move, board_string_to_matrix

from player import players


api = FastAPI()


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
    board_matrix = board_string_to_matrix(board_string)
    best_move = find_best_move(board_matrix, players[player])
    return best_move
