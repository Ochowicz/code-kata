def to_freud(sentence):
    lista = sentence.split()
    for i in range(len(lista)):
        lista[i] = 'sex'
    return ' '.join(lista)