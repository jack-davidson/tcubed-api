from fastapi import FastAPI, Response

from fastapi.responses import HTMLResponse, JSONResponse

from fastapi.middleware.cors import CORSMiddleware

from markdown import markdown

from board import board_string_to_matrix, board_matrix_to_string, eval_board, minimax, find_best_move

from player import Player, players


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
def board(board_string, player, response):
    return find_best_move(board_string_to_matrix(board_string), player, player == 'X' ? 'O' : 'X')


@api.get("/test/board_matrix_to_string")
def test_board_matrix_to_string():
    return board_matrix_to_string([[Player.E] * 3] * 3)


@api.get("/test/eval_board")
def test_eval_board():
    return eval_board([[Player.O] * 3] * 3)


@api.get("/test/minimax")
def test_minimax():
    return minimax(board_string_to_matrix("XOXEEEOXO"), 0, Player.X)


@api.get("/test/toggle_player")
def test_toggle_player():
    return Player.toggle(Player.X)
