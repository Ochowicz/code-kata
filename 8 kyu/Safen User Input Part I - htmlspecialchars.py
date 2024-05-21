def html_special_chars(data):
    # Definiowanie mapowania znaków
    translation_table = str.maketrans({
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        '&': '&amp;'
    })

    # Zamiana znaków w tekście za pomocą metody translate()
    return data.translate(translation_table)