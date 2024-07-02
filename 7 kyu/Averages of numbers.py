def averages(arr):
    return [(i + j) / 2 for i, j in zip(arr, arr[1:])] if arr else []