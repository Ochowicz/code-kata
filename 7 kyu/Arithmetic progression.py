def arithmetic_sequence_elements(a, d, n):
    try:
        return ', '.join(str(i) for i in range(a, a+d*n, d))
    except:
        return ', '.join([str(a)] * n)