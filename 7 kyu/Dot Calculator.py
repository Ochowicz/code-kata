import re
def calculator(txt):
    dots = re.findall(r'\.+', txt)
    operator = re.findall(r'[^\.]+', txt)
    return (eval(str(len(dots[0])) + operator[0] + str(len(dots[1])))) * '.'