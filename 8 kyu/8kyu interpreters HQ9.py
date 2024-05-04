def bottles_of_beer():
    lyrics = ''
    for i in range(99, 0, -1):
        if i > 1:
            lyrics += f"{i} bottles of beer on the wall, {i} bottles of beer.\n"
            lyrics += f"Take one down and pass it around, {i-1} bottle{'s' if i-1 != 1 else ''} of beer on the wall.\n"
        else:
            lyrics += "1 bottle of beer on the wall, 1 bottle of beer.\n"
            lyrics += "Take one down and pass it around, no more bottles of beer on the wall.\n"
    lyrics += "No more bottles of beer on the wall, no more bottles of beer.\n"
    lyrics += "Go to the store and buy some more, 99 bottles of beer on the wall."
    return lyrics
def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return 'Q'
    elif code == '9':
        return bottles_of_beer()
    else:
        return None