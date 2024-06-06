def solve(s):
    lower = sum(c.islower() for c in s)
    upper = sum(c.isupper() for c in s)
    return s.lower() if lower >= upper else s.upper()