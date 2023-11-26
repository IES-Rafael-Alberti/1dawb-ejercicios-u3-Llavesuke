
DICTIONARY = {}

def ask_words():

    words = input('Palabra:Traduccion y cada par separados por comas \n -> ')

    translated_words = words.split(',')

    for translated_word in translated_words:
        key,value = translated_word.split(':')
        DICTIONARY.setdefault(key,value)

def translate_phrase():
    translated_phrase = []

    phrase = input('Introduzca una frase para traducir \n -> ').split()
    
    for word in phrase:
            translated_word = DICTIONARY.get(word,word)

            translated_phrase.append(translated_word)


    print((' '.join(translated_phrase)))
    
def main():
    ask_words()
    translate_phrase()

if __name__ == "__main__":
    main()