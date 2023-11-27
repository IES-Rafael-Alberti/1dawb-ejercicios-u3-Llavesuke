
def ask_students_elementary():
    student = None
    elementary_students = []
    while student != 'X':

        student = input('Nombre de alumno de primaria -> ').title()

        if student != 'X':
            elementary_students.append(student)
    
    return set(elementary_students)

def ask_students_secondary():
    student = None
    secondary_students = []

    while student != 'X':

        student = input('Nombre de alumno de secundaria -> ').title()

        if student != 'X':
            secondary_students.append(student)

    return set(secondary_students)

def show_students(elementary_students,secondary_students):

    print('Nombres de los alumnos de primaria y secundaria:')
    print(elementary_students|secondary_students)

    print('Nombres en comun')
    print(elementary_students&secondary_students)

    print('Nombres de primaria que no se repiten en secundaria')
    if elementary_students-secondary_students == {}:
        print('Ninguno se repite')
    else:
        print(elementary_students-secondary_students)

    if elementary_students <= secondary_students:
        print('Si estan todos incluidos')
    else:
        print('No todos los nombres de primaria estan incluidos en los de secundaria')

def main():
    elementary_students = ask_students_elementary()

    secondary_students = ask_students_secondary()

    show_students(elementary_students,secondary_students)

if __name__ == "__main__":
    main()
