def capitalize(s, ind):
    lst = list(s)
    for i in ind:
        if i < len(lst):
            lst[i] = lst[i].upper()
    return ''.join(lst)