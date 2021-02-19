from fastapi import FastAPI, Response, status

from fastapi.responses import HTMLResponse, JSONResponse

from fastapi.middleware.cors import CORSMiddleware

from markdown import markdown

from board import board_string_to_matrix

from errors import Errors

import config

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
    return board_string_to_matrix(board_string)
