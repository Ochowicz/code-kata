def validate_hello(greetings):
    greets = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czes']
    for greet in greets:
        if greet in greetings.lower():
            return True
    return False