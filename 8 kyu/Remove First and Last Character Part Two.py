def array(string):
    array = string.split(',')
    if len(array) < 3:
        return None
    return ' '.join(array[1:-1])