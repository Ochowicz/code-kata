def men_from_boys(arr):
    arr = list(set(arr))
    even = sorted([x for x in arr if x % 2 == 0])
    odd = sorted([y for y in arr if y % 2 != 0], reverse=True)
    return even + odd