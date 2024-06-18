def adjacent_element_product(array):
    return max(array[n] * array[n+1] for n in range(len(array) - 1))