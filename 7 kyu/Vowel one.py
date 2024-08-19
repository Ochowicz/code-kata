def vowel_one(s):
    return ''.join('1' if i.lower() in 'aeiou' else '0' for i in s)