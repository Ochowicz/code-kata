def vert_mirror(lst):
    return '\n'.join(''.join(reversed(i)) for i in lst)


def hor_mirror(lst):
    return '\n'.join(reversed(lst))


def oper(fct, s):
    lst = s.split('\n')
    return fct(lst)