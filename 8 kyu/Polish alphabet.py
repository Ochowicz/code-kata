def correct_polish_letters(st):
    change = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'z',
        'ż': 'z'
        }
    string = ''
    for letter in st:
        if letter in change:
            string += change[letter]
        else:
            string += letter
    return string