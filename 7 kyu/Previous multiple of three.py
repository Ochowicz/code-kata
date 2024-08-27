def prev_mult_of_three(n):
    while n % 3 != 0 and n != 0:
        n = str(n)[:-1]
        if n == '':
            return None
        n = int(n)
    return n if n != 0 else None