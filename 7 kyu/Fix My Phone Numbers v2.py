import re
def is_it_a_num(s: str) -> str:
    d = ''.join(re.findall(r'\d', s))
    return d if len(d) == 11 and d[0] == '0' else "Not a phone number"