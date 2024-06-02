def is_isogram(string):
    if string == '':
        return True
    return sorted(list(string.lower())) == sorted(set(string.lower()))