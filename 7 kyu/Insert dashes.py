def insert_dash(num):
    num_str = str(num)
    result = []
    for i in range(len(num_str)):
        result.append(num_str[i])
        if i < len(num_str) - 1 and int(num_str[i]) % 2 == 1 and int(num_str[i + 1]) % 2 == 1:
            result.append('-')
    return ''.join(result)