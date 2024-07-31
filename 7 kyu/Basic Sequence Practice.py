def sum_of_n(n):
    if n >= 0:
        return [sum(range(x+1)) for x in range(n+1)]
    else:
        return [-sum(range(x+1)) for x in range(-n+1)]