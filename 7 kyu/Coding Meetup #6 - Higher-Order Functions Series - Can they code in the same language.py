def is_same_language(lst):
    return len(set(i['language'] for i in lst)) == 1