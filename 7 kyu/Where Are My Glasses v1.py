import re
def find_glasses(lst):
    for i, v in enumerate(lst):
        if re.search(r'O-+O', v):
            return i