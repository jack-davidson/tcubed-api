# tcubed api documentation

## routes

### `board/<board>/turn/<turn>`
`GET /board/<board_string>/turn/<turn> -> "[<x>, <y>]"`

Given the current board `<board_string>` and current turn `<turn>`, choose the
best move and return json encoded coordinates of the best move.

`<turn>` may be `X` or `O`

`<board>` is encoded as a string where:
```
url encoded | representation in program
---------------------------------------
E           | EMPTY
X           | X
O           | O
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
