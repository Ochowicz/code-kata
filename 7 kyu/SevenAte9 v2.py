import re
def seven_ate9(str_):
    result = re.sub(r'79(?=7)', '7', str_)
    return result