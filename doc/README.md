# tcubed api documentation

The tcubed api interacts with the ai and frontend.

## routes

### `board/<board>`
`GET /board/<board> -> "{ "X", "O", "EMPTY", ... }"`

Given the current board `<board>`, choose the best move
and return json encoded string of the board with the next
move complete.

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
