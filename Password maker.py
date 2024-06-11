import re
def make_password(phrase):
    password = ''
    for word in phrase.split():
        if word.lower()[0] == 'i':
            password += '1'
        elif word.lower()[0] == 'o':
            password += '0'
        elif word.lower()[0] == 's':
            password +='5'
        else:
            password += word[0]
    return password