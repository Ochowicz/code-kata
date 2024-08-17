def create_dict(keys, values):
    return dict.fromkeys(keys) | dict(zip(keys,values))