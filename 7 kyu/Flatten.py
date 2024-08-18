def flatten(lst):
    return [item for sublist in lst for item in (sublist if isinstance(sublist, list) else [sublist])]