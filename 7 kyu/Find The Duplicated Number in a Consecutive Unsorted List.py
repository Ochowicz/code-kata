def find_dup(arr):
    arr.sort()
    return next(i for i, j in zip(arr, arr[1:]) if i == j)