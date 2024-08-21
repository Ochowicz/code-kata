def sum_no_duplicates(l):
    no_duplicates = []
    duplicates = []
    for i in l:
        if i not in no_duplicates:
            no_duplicates.append(i)
        else:
            duplicates.append(i)
    return sum(x for x in l if x not in duplicates)