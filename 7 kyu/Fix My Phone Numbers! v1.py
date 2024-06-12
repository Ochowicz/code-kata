def is_it_a_num(s: str) -> str:
    number = ''.join(list(filter(lambda n: n.isdigit(), s)))
    return number if len(number) == 11 and number[0] == '0' else "Not a phone number"