def count_languages(lst):
    language_count = {}
    for dev in lst:
        language = dev['language']
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1
    return language_count