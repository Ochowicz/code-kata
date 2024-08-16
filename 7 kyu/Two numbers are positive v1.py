def two_are_positive(a, b, c):
    [a, b, c] = sorted([a, b, c])
    return a <= 0 and b > 0