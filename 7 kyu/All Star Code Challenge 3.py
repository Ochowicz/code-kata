import re

def remove_vowels(strng):
    result = re.sub(r'[aeiou]', '', strng, flags=re.IGNORECASE)
    return result