def seven(m):
    num = m
    step = 0
    while num > 99:
        num = num // 10 - 2 * (num % 10)
        step += 1
    return (num, step)