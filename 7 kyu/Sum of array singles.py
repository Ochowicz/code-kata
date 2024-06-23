def repeats(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return sum(num for num in arr if counts[num] == 1)