import re

def initialize_names(name):
    return re.sub(' (.).*?(?= )', r' \1.', name)