def solve(n):
    nominały = [500, 200, 100, 50, 20, 10]
    banknoty = 0
    for nominał in nominały:
        if n == 0:
            break
        if n >= nominał:
            banknoty += n // nominał
            n = n % nominał
    if n == 0:
        return banknoty
    else:
        return -1
