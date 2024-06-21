def filter_string(st):
    number = ''
    for char in st:
        try:
            int(char)
            number += char
        except:
            pass
    return int(number)