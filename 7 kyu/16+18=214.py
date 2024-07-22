def add(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    max_len = max(len(num1_str), len(num2_str))
    num1_str = num1_str.zfill(max_len)
    num2_str = num2_str.zfill(max_len)
    result = [str(int(x) + int(y)) for x, y in zip(num1_str, num2_str)]
    return int(''.join(result))