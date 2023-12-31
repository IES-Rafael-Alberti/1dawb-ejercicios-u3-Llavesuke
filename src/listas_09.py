from src.listas_08 import ask_word

def count_vowels(word:str) -> list:
    """Count vowels in a word.

    Args: 
        word (str): The word written by the user.
    
    Returns:
        lista (list[int]): A list with integers of the vowels counted.
    """
    lista = []

    for vocal in 'aeiou':
        count = word.count(vocal)
        lista.append(count)

    return lista

def main():

    word = ask_word()

    vowels_list = count_vowels(word) # type: ignore
    bool = True
    
    print('----------------------------')
    for i in range(len(vowels_list)):
        while bool:
            for vocal in 'aeiou':
                print(f'En la palabra {word}, hay {vowels_list[i]} {vocal}')
                bool = False
                i +=1
    print('----------------------------')

if __name__ == "__main__":
    main()