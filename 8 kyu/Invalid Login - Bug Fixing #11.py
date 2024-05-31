def validate(username, password):
    if '||' in password or '//' in password:
        return "Wrong username or password!"
    else:
        return Database().login(username, password)