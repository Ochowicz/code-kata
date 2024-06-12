import re

search = re.compile(r"((?=\w+$)\w+|\w)\w*").findall

def initials(name):
    return '.'.join(search(name)).title()