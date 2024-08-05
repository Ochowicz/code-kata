import re

def find_glasses(lst):
    return next(i for i, v in enumerate(lst) if re.search(r'O-+O', v))