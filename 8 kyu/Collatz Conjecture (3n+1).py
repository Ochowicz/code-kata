def hotpo(n):
    num = 0
    while n != 1:
        if n % 2 == 0:
            n = n/2
            num += 1
        else:
            n = 3 * n + 1
            num += 1
    return num