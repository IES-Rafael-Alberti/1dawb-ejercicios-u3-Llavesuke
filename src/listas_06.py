from listas_02 import ask_subject
from listas_03 import ask_marks, clean_terminal

def check_approved(subjects,marks):
    """Check each subject with its corresponding mark.

    Args:
        subjects (list[str]): A list with the subjects written by the user.
        marks (list Union[float,int]) : A list with integers and floats values.
    """
    for i in range(len(subjects) -1, -1, -1):
        if marks[i] < 5:
            subjects.pop(i)
    
    return subjects

def main():

    subjects = ask_subject()

    clean_terminal()

    print(f'\n{subjects}\n')
    marks = ask_marks(subjects)

    approved_list = check_approved(subjects,marks)

    clean_terminal()
    
    if len(approved_list) == 1:
        print(f'Solo has aprobado {approved_list}')
    else:
        print(f'Tus asignaturas aprobadas son: {approved_list}')

if __name__ == "__main__":
    main()