def show_sequence(n):
    return '+'.join(str(n) for n in range(n+1)) + ' = ' + str(sum(n for n in range(n+1))) if n > 0 else f'{n}<0' if n < 0 else '0=0'