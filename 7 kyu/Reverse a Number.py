def reverse_number(n):
    if str(n)[0] == '-':
        return int(f'-{str(-n)[::-1]}')
    return int(str(n)[::-1])