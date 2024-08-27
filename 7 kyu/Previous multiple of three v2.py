def prev_mult_of_three(n):
    while n % 3:
        n //= 10
    return n or None