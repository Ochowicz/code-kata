def number_to_pwr(number, p):
    if p == 0:
        return 1
    result = 1
    for i in range(p):
        result *= number
    return result
