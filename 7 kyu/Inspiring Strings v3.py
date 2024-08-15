def longest_word(string_of_words):
    return max(reversed(string_of_words.split()), key=len)