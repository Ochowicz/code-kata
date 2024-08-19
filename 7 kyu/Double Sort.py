def db_sort(arr):
    numbers = sorted([x for x in arr if isinstance(x, (int, float))])
    strings = sorted([x for x in arr if isinstance(x, str)])
    return numbers + strings