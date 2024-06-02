import re
def printer_error(s):
    return f"{len(re.findall(r'[n-z]', s))}/{len(s)}"
    #return f"{len([char for char in s if char in 'noprstquvwxyz'])}/{len(s)}"