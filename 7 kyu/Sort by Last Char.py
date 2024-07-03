def last(s):
    lst = s.split()
    lst.sort(key=lambda x: x[-1])
    return lst