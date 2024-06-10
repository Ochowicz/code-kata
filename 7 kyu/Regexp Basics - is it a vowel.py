import re
def is_vowel(s):
    return bool(re.match(r'[aeiou]\Z', s, re.I))