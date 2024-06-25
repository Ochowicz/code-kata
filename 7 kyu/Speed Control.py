def gps(s, x):
    return max(((i - j) for i, j in zip(x[1:], x)), default=0) / (s / 3600)