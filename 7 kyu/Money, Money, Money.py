def calculate_years(principal, interest, tax, desired):
    p, i, t, d = (principal, interest, tax, desired)
    y = 0
    while p < d:
        p += p * i * (1 - t)
        y += 1
    return y