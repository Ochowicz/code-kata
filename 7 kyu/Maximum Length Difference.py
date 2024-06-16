def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    min_len_a1 = min(map(len, a1))
    max_len_a1 = max(map(len, a1))
    min_len_a2 = min(map(len, a2))
    max_len_a2 = max(map(len, a2))
    return max((max_len_a1 - min_len_a2), (max_len_a2 - min_len_a1))