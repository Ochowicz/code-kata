import re
def initials(name):
    return re.sub(r'\b(\w)(\w+)\b\s', r'\1.', name.title())