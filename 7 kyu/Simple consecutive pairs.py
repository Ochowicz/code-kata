def pairs(arr):
    return sum(1 for i, j in zip(arr[::2], arr[1::2]) if abs(i - j) == 1)