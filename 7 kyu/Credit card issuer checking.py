import re
def get_issuer(number):
    num_str = str(number)
    if re.match(r'^3[47]', num_str) and len(num_str) == 15:
        return 'AMEX'
    elif re.match(r'^6011', num_str) and len(num_str) == 16:
        return 'Discover'
    elif re.match(r'^5[1-5]', num_str) and len(num_str) == 16:
        return 'Mastercard'
    elif re.match(r'^4', num_str) and len(num_str) in [13, 16]:
        return 'VISA'
    else:
        return 'Unknown'