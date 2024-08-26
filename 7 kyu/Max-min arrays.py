def solve(arr):
    arr_sorted = sorted(arr)
    max_vals = arr_sorted[::-1]
    min_vals = arr_sorted
    result = []

    for i in range(len(arr)):
        if i % 2 == 0:
            result.append(max_vals[i // 2])
        else:
            result.append(min_vals[i // 2])

    return result