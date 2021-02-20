from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from markdown import markdown

from board import deserialize_board, best_move

from square import perfect_square

from player import Player

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
def board(board_string: str, player: str, response: Response):
    if not perfect_square(len(board_string)):
        return {"error": "length(board_string) not perfect square"}

    return best_move(deserialize_board(board_string),
                     Player.string(Player.player(player)),
                     Player.string(-Player.player(player)))
