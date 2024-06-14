import re
def password(string):
    lst = list(string)
    digit, upper, lower = 0, 0, 0
    if len(string) < 8:
        return False
    for char in lst:
        if char.isdigit():
            digit += 1
        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1
    return bool(digit) and bool(upper) and bool(lower)