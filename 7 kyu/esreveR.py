def reverse(lst):
    empty_list = list()
    for i in range(len(lst)-1, -1, -1):
        empty_list.append(lst[i])
    return empty_list