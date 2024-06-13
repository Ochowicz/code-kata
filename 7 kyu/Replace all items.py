def replace_all(obj, find, replace):
    return [i if i != find else replace for i in obj] if isinstance(obj, list) else obj.replace(find, replace)