def alias_gen(first_name, last_name):
    # Check if the first character of each name is a letter
    if not first_name[0].isalpha() or not last_name[0].isalpha():
        return "Your name must start with a letter from A - Z."
    else:
        return f'{FIRST_NAME[first_name[0].upper()]} {SURNAME[last_name[0].upper()]}'