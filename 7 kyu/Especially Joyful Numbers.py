def number_joy(n):
    sum_of_digits = sum(map(int, str(n)))
    return n % sum_of_digits == 0 and sum_of_digits * int(str(sum_of_digits)[::-1]) == n