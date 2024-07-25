import re
def seven_ate9(str_):
    result = re.sub(r'797', '77', str_)
    result = re.sub(r'797', '77', result)
    return result