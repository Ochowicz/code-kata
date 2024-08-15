def longest_word(string_of_words):
    longest = ''
    letters = 0
    for word in string_of_words.split():
        if len(word) >= letters:
            letters = len(word)
            longest = word
    return longest