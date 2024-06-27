def find_digit(num, nth):
    if nth <= 0:
        return -1
    return int(str(num)[-nth]) if nth <= len(str(abs(num))) else 0