def freq_seq(s, sep):
    return f'{sep}'.join(str(s.count(i)) for i in s)