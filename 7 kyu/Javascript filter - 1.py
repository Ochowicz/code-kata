def ends_with_underscore(pair):
    return pair[0].endswith('_')

def search_names(logins):
    return list(filter(ends_with_underscore, logins))