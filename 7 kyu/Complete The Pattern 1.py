def pattern(n):
    result = ''
    if n > 0:
        for i in range(1, n + 1):
            result += f'{i}' * i + '\n'
    return result.rstrip()