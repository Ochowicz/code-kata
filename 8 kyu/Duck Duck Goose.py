# The objective of Duck, duck, goose is to walk in a circle, tapping on each player's head until one is chosen.
#
# Task: Given an array of Player objects (an array of associative arrays in PHP) and an index (1-based), return the name of the chosen Player(name is a property of Player objects, e.g Player.name)
#
# Example:
#
# duck_duck_goose([a, b, c, d], 1) should return a.name
# duck_duck_goose([a, b, c, d], 5) should return a.name
# duck_duck_goose([a, b, c, d], 4) should return d.name
# // PHP only
# duck_duck_goose([$a, $b, $c, $d], 1); // => $a["name"]
# duck_duck_goose([$a, $b, $c, $d], 5); // => $a["name"]
# duck_duck_goose([$a, $b, $c, $d], 4); // => $d["name"]

class Player:
    def __init__(self, name):
        self.name = name


ex_names = ["a", "b", "c", "d", "c", "e", "f", "g", "h", "z"]
players = list(map((lambda x: Player(x)), ex_names))

print(players)

def duck_duck_goose(players, goose):
    return players[goose % len(players)-1].name
