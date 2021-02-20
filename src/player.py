# player enum
class Player:
    E = 0
    X = 1
    O = 2

    def toggle(player: 'Player') -> 'Player':
        return Player.O if player is Player.X else Player.X


# player lookup
players = {
    'E': Player.E,  # E: Empty
    'X': Player.X,  # X: player 'X'
    'O': Player.O,  # O: player 'O'
}


# reverse player lookup
reverse_players = {
    value: key for (key, value) in players.items()
}
