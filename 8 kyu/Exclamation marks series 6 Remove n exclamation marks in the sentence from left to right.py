def remove(st, n):
    result = ''
    for char in st:
        if n > 0 and char == '!':
            result += ''
            n += -1
        else:
            result += char
    return result