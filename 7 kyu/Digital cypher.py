def encode(message, key):
    """Funkcja szyfrująca wiadomość z użyciem klucza"""

    # Zamiana klucza na listę cyfr
    key_digits = [int(digit) for digit in str(key)]

    # Zaszyfrowana wiadomość
    encoded_message = []

    for i, char in enumerate(message):
        # Zamiana liter wiadomości na odpowiedniki liczbowe
        char_value = ord(char) - ord('a') + 1
        # Dodanie odpowiedniej cyfry z klucza (w cyklu)
        encoded_value = char_value + key_digits[i % len(key_digits)]
        # dodatnie zaszyfrowaneej wartości do listy
        encoded_message.append(encoded_value)

    # Zwrócenie zaszyfrowanej wartości
    return encoded_message