def sum_digits(number):
    return sum(int(n) for n in str(abs(number)))