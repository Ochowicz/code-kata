def create_dict(keys, values):
    dic = {}
    while len(keys) > len(values):
        values.append(None)
    for k, v in zip(keys, values):
        dic[k] = v
    return dic