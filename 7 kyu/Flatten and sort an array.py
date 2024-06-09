def flatten_and_sort(array):
    result =[]
    for arr in array:
        for value in arr:
            result.append(value)
    return sorted(result)