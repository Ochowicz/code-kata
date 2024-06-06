import re
def solve(s):
    return s.lower() if s.count(r'a-z') >= s.count(r'A-Z') else s.upper()
print('aaaBB'.count(r'[a-z]'))