def _all(seq, func):
    return all(func(item) for item in seq) if seq else True