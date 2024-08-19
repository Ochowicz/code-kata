def even_last(numbers):
    return sum(numbers[::2]) * numbers[-1] if numbers else 0