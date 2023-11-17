import os
from src.listas_02 import ask_subject

def ask_marks(subjects:list[str]) -> list[int]:
    """Ask the marks from the previous subjects

    Ask the marks from the subjects written by the user and ends when
    the numbers of the grades its the same as the name of subjects.

    Args:
        subjects (list[str]): A list of subjects written by the user.

    Returns:
        marks (list[int]): A list with the marks of each subject.

    Raises:
        ValueError: If the input is a integer or a float.
    
    """
    marks = []
    mark = None

    while not len(subjects) == len(marks):
        try:  
        
            mark = float(input('Introduce una nota(exit para salir) -> '))
            
           
            marks.append(mark)
        
        except ValueError:
            print('No puedes introducir texto')

    return marks

def loops(subjects,marks):
    for i in range (0,len(marks)):
        print(f'En {subjects[i]} has sacado un {marks[i]}')


def clean_terminal():
    """Clean the terminal

    Will print in the terminal a command depending of the operating system.
    
    """
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

def main():

    subjects = ask_subject()

    clean_terminal()

    print(f'\n{subjects}\n')
    marks = ask_marks(subjects)

    loops(subjects,marks)

if __name__ == "__main__":
    main()