def longest_word(s):
    return sorted(s.split(), key = len)[-1]