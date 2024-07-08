def pairs(arr):
    return sum(abs(i - j) == 1 for i, j in zip(arr[::2], arr[1::2]))