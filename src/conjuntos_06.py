import string


def listAlphabet():
    return list(string.ascii_lowercase)

if __name__ == "__main__":
    vocales = {'a', 'e', 'i', 'o', 'u'}
    abecedario = set(listAlphabet())
    consonantes = abecedario - vocales 

    letras_comun = consonantes.union(vocales)
    print(letras_comun)