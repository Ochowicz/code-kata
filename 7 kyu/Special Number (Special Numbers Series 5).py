import re

def special_number(number):
    lst = re.findall(r'[6789]', str(number))
    return 'Special!!' if lst == [] else 'NOT!!'