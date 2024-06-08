def factorial(n):
    if n < 0 or n > 12:
        raise ValueError("Input must be between 0 and 12")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result