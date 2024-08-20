def initialize_names(name):
    lst = name.split(' ')
    return name if len(lst) <= 2 else lst[0] + ' ' + ' '.join(f'{x[0]}.' for x in lst[1:-1]) + ' ' + lst[-1]