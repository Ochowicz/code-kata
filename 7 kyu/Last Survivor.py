
def last_survivor(letters, coords):
    coords = coords[::-1]
    while coords:
        i = coords.pop()
        letters = letters[:i] + letters[i+1:]
    return letters