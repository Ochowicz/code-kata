def squares(x, n):
    result = []
    while n > 0:
        result.append(x)
        x **= 2
        n -= 1
    return result