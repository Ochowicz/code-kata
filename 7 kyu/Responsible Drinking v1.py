import re
def hydrate(drink_string):
    x = sum(map(int, re.findall(r'[\d]', drink_string)))
    return f"{x} glass{'es' if x > 1 else ''} of water"