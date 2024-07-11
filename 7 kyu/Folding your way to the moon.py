def fold_to(distance):
    if distance < 0:
        return None
    t = 0.0001
    n = 0
    while t < distance:
        t *= 2
        n += 1
    return n