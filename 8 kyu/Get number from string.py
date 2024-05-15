def get_number_from_string(st):
    number = ''
    for i in st:
        if i.isdigit():
            number += i
    try:
        return int(number)
    except:
        return None