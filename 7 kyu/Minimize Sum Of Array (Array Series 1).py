def min_sum(arr):
    return sum(i * j for i, j in zip(sorted(arr), sorted(arr)[::-1]))/2