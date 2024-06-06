def capitals(word):
    return [i for i, c in enumerate(word, 0) if ord(c) < ord('a')]