#!/usr/bin/env python3
import flask
import markdown
import math
import json

app = flask.Flask(__name__)

# player lookup
players = {
    "E": 0,  # E: Empty
    "X": 1,  # X: player 'X'
    "O": 2,  # O: player 'O'
}


def api_response(obj):
    return flask.Response(json.dumps(obj), mimetype="application/json")


def board_rows(board_len: str) -> int:
    return int(math.sqrt(board_len))


def deserialize_board(board: str) -> list[list[int]]:
    rows = board_rows(len(board))

    return [
        [None for i in range(rows)]
        for i in range(rows)
    ]


def eval_board(board: list[list[int]]) -> int:
    if board[0] and board[1] and board[2] == players["X"]:
        return 0


@app.route("/board/<board>/turn/<turn>")
def board(board, turn):
    return api_response(deserialize_board(board))


@app.route('/')
def home():
    with open("../doc/api_home.md", "r") as fd:
        api_home = fd.read()
        fd.close

    return markdown.markdown(api_home)


if __name__ == "__main__":
    app.run(debug=True)
