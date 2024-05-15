def parse_float(input_data):
    if isinstance(input_data, str):
        try:
            return float(input_data)
        except ValueError:
            return None
    elif isinstance(input_data, list):
        try:
            return float(''.join(map(str, input_data)))
        except ValueError:
            return None
    else:
        return None