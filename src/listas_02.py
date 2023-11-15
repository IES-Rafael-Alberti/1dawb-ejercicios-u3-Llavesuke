
from listas_01 import ask_subject

def loop_subjects(subjects):
    """Print each subject on the list

    Args:
        subjects (List[strings]): A list with the subjects written by the user.
    """
    for subject in subjects:
        print(f'\nYo estudio {subject}')

def main():
    
    subjects = ask_subject()

    loop_subjects(subjects)
        
if __name__ == "__main__":
    main()