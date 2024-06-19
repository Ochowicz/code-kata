def power_of_two(x):
    if x <= 0:
        return False
    while x % 2 == 0:
        x //= 2
    return x == 1