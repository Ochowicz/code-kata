def triple_x(s):
    for i, char in enumerate(s):
        if char == 'x':
            return s[i+1:i+3] == 'xx'
    return False