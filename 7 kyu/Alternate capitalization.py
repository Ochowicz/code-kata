def capitalize(s):
    odd = ''
    even = ''
    for i, char in enumerate(s):
        if i % 2 == 0:
            even += char.upper()
            odd += char
        else:
            even += char
            odd += char.upper()
    return [even, odd]