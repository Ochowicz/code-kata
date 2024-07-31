import re
def solve(s):
    lst = re.findall(r'[aeiou]+', s)
    return max(map(len, lst), default=0)