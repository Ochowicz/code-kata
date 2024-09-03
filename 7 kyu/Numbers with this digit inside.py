def numbers_with_digit_inside(x, d):
    count = 0
    total_sum = 0
    total_product = 1

    for i in range(1, x + 1):
        if str(d) in str(i):
            count += 1
            total_sum += i
            total_product *= i

    if count == 0:
        return [0, 0, 0]

    return [count, total_sum, total_product]