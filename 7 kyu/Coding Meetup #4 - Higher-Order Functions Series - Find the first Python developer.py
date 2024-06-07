def get_first_python(users):
    for dev in users:
        if dev["language"] == "Python":
            return f'{dev["first_name"]}, {dev["country"]}'
    return 'There will be no Python developers'