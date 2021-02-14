# tcubed api documentation

The tcubed api interacts with the ai and frontend.

## routes

### `board/<board>/<size>/<turn>`
`GET /board/<board>/<size>/<turn> -> "{ "X", "O", "EMPTY", ... }"`

Given the current board `<board>`, choose the best move
and return json encoded string of the board with the next
move complete.

`<turn>` may be `X` or `O`

`<size>` is the amount of rows or columns in the board (they should be equal
in a square board so you may choose either)

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
