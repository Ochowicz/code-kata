def row_weights(array):
    team1_weight = sum(a for i, a in enumerate(array) if i % 2 == 0)
    team2_weight = sum(a for i, a in enumerate(array) if i % 2 != 0)
    return (team1_weight, team2_weight)