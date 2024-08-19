def save(sizes, hd):
    used_capacity = 0
    files = 0
    for i in sizes:
        if used_capacity + i <= hd:
            used_capacity += i
            files += 1
        else:
            break
    return files