def is_divisible(*a):
    return all(a[0] % a[i] == 0 for i in range(1, len(a)))