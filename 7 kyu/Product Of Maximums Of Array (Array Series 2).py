def max_product(lst, n_largest_elements):
    num = 1
    for i in sorted(lst)[-n_largest_elements:]:
        num *= i
    return num