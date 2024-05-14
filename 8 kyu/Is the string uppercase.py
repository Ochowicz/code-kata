def is_uppercase(inp):
    return all(c.isupper() or not c.isalpha() for c in inp)