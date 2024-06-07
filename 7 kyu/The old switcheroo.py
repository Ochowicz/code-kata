def vowel_2_index(string):
    lst = list(string)
    for i in range(len(string)):
        if lst[i].lower() in 'aeiou':
            lst[i] = str(i + 1)
    return ''.join(lst)