def series_sum(n):
    return f"{sum([1 / (3 * n + 1) for n in range(n)]):.2f}"