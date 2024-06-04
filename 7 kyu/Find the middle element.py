def gimme(input_array):
    return [n for n in [0, 1, 2] if n not in ((input_array.index(min(input_array)), input_array.index(max(input_array))))][0]