
def ask_word():
    """Ask the user for a word.

    Returns:
        word (list[str]): The word written by the user converted in a list with each character being a value of it.
    Raises:
        ValueError: If the input is a integer or a float.
    """
    flow_control = False

    while not flow_control:
        try:  
        
            word = input('Introduce una palabra -> ')
            
            if word.isdigit() or (word.replace('.','')).isdigit(): #Delete the point and its treated as a int for classify it.
                raise ValueError
            
            else:
                flow_control = True
                word = list(word.lower())

                return word
        
        except ValueError:
            print('No puedes introducir números')

def palindrome(word):
    """Check if the word is a palindrome

    Args:
        word (list[str]): The word written by the user converted in a list with each character being a value of it.
    
    Returns:
        True (bool): When the word is a palindrome.
        False (bool): When the word is not a palindrome.
    """
    reversed_word = list(word)
    reversed_word.reverse()

    if word == reversed_word:
        return True
    else:
        return False

    
def main():
    
    word = ask_word()

    if palindrome(word):
        print('----------------------------')
        print('La palabra si es palindroma')
        print('----------------------------')
    else:
        print('----------------------------')
        print('No es palindroma')
        print('----------------------------')

if __name__ == "__main__":
    main()