
def ask_subject():
    """Ask the user for subjects until, she/he writes exit.

    Raises:
        ValueError: If the input is a integer or a float.
    """
    Subjetcs = []
    subject = None

    while not subject == 'exit':
        try:  
        
            subject = input('Introduce una asignatura (exit para salir) -> ')
            
            if subject.lower() == 'exit':
                return Subjetcs
            
            if subject.isdigit() or (subject.replace('.','')).isdigit(): #Delete the point and its treated as a int for classify it.
                raise ValueError
            
            else:
        
                Subjetcs.append(subject)
        
        except ValueError:
            print('No puedes introducir números')

def main():
    
    print(ask_subject())
        
if __name__ == "__main__":
    main()