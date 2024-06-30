def add_letters(*letters):
    if not letters:
        return 'z'
    total = sum((ord(letter) - ord('a') + 1) for letter in letters)
    result = (total - 1) % 26 + 1
    return chr(result + ord('a') - 1)