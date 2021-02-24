class Player:
    O = -1
    E = 0
    X = 1


turns = {'O': Player.O, 'E': Player.E, 'X': Player.X}
reverse_turns = {value: key for (key, value) in turns.items()}


# convert string to Player
def deserialize(player: str) -> int:
    return turns[player]


# convert Player to string
def serialize(player: 'Player') -> str:
    return reverse_turns[player]
