# tcubed api documentation

## routes

### `board/<board>/player/<player>`
`GET /board/<board_string>/player/<player> -> "[<x>, <y>]"`

Given the current board `<board_string>` and current player `<player>`, choose the
best move and return json encoded coordinates of the best move.

`<player>` may be `X` or `O`

`<board>` is encoded as a string where:
```
url encoded | representation in program
---------------------------------------
E           | EMPTY
X           | X player (maximizer)
O           | O player (minimizer)
```
for example, a tic tac toe board:
```
X O X
_ X O
O _ X
```
would be encoded as:
```
XOXEXOOEX
```
