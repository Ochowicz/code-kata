def catch_sign_change(lst):
    return sum((str(i) + str(j)).count('-') == 1 for i, j in zip(lst, lst[1:]))
