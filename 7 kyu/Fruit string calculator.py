import re
def calculate(strng):
    digits = tuple(map(int, re.findall(r'\d+', strng)))
    return sum(digits) if 'gains' in strng else digits[0] - digits[1]