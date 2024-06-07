import re
def remove_consecutive_duplicates(s : str) -> str:
    pattern = r'\b(\w+)( \1)+\b'
    result = re.sub(pattern, r'\1', s)
    return result