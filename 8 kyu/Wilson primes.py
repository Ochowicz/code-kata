from math import factorial
def am_i_wilson(n):
    if n < 2 or n > 1000:
        return False
    return (factorial(n - 1) + 1) % (n * n) == 0