def well(x):
    i = x.count('good')
    if i == 0:
        return 'Fail!'
    elif i <= 2:
        return 'Publish!'
    else:
        return 'I smell a series!'