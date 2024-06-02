def disemvowel(string_):
    result = ''
    for char in string_:
        if char.lower() not in 'aeiou':
            result += char
    return result