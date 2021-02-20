class Player:
    O = -1
    E = 0
    X = 1

    players = {'O': O, 'E': E, 'X': X}
    reverse_players = {value: key for (key, value) in players.items()}

    # convert string to Player
    def player(player: str) -> int:
        return Player.players[player]

    # convert Player to string
    def string(player: 'Player') -> str:
        return Player.reverse_players[player]
