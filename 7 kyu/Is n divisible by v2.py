def is_divisible(n, *a):
    return all(n % i == 0 for i in a)