import textwrap

# Twój tekst
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

# Zawijanie tekstu do wierszy o szerokości 20 znaków
wrapped_text = textwrap.wrap(text, width=79)

# Wyświetlenie wyniku
for line in wrapped_text:
    print(line)