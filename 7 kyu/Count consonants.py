def consonant_count(s):
    return len([i for i in s if i.isalpha() and i.lower() not in 'aeiou'])