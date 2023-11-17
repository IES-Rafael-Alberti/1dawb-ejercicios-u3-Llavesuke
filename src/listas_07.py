from listas_06 import clean_terminal

def check_3(letters:list[str]):
    """Check each letter and if its position its a 3 multiple, delete it.

    Args:
        letters (list[str]): A list with the letters written by the user.
    Results:
        removed_letters (list[str]): A list with the comprobation already did.
    """
    for i in range(len(letters),-1,-1):
        if  i%3 == 0:
            del(letters[i])
    
    return letters

def main():

    letters = list(chr(i) for i in range (97,123))

    print(f'\n{letters}\n')

    checked_list = check_3(letters)
    
    print(checked_list)

if __name__ == "__main__":
    main()