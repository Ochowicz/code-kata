def my_languages(results):
    filtered_results = filter(lambda item: item[1] >= 60, results.items())
    sorted_results = sorted(filtered_results, key=lambda item: item[1], reverse=True)
    return [language for language, score in sorted_results]