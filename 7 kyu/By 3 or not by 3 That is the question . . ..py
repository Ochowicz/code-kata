def divisible_by_three(st):
    digit_sum = sum(int(i) for i in st)
    while digit_sum >= 3:
        digit_sum -= 3
    return digit_sum == 0