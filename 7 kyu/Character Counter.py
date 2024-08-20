def validate_word(word):
    lst = [word.lower().count(l) for l in dict.fromkeys(word.lower())]
    return sum(lst)/len(lst) == lst[0]