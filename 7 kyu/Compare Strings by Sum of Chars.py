def compare(s1, s2):
    if s1 is None:
        s1 = ''
    if s2 is None:
        s2 = ''
    if s1.isalpha() and s2.isalpha():
        return sum(map(ord, s1.upper())) == sum(map(ord, s2.upper()))
    elif s1.isalpha() or s2.isalpha():
        return False
    else:
        return True