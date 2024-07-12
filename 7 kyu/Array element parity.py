def solve(arr):
    return next(x for x in arr if -x not in arr)