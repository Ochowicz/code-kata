def get_strings(city):
    return ','.join(f"{l}:{'*' * city.lower().count(l)}" for l in dict.fromkeys(city.lower()) if l.isalpha())