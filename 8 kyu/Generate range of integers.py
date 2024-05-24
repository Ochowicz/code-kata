def generate_range(start, stop, step):
    result = []
    for i in range(start, stop + 1, step):
        result.append(i)
    return result