def max_gap(numbers):
    numbers.sort()
    return max(j - i for i, j in zip(numbers, numbers[1:]))