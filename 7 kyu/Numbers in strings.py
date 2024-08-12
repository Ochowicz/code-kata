import re
def solve(s:str) -> int:
    lst = re.findall(r'[0-9]+', s)
    return max(map(int, lst))