from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from markdown import markdown

import board

import square

import turn

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


# receives board encoded as string and current player
# returns coordinates of best move
@api.get("/board/{board_string}/player/{player}", response_class=JSONResponse)
def ai(board_string: str, player: str, response: Response):
    if not square.perfect_square(len(board_string)):
        return {"error": "length(board_string) not perfect square"}

    board_matrix = board.deserialize(board_string)
    current_turn = turn.deserialize(player)

    return board.best_move(board_matrix, current_turn)
