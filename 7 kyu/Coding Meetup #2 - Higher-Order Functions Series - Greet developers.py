def greet_developers(lst):
    for dev in lst:
        dev['greeting'] = f"Hi {dev['firstName']}, what do you like the most about {dev['language']}?"
    return lst