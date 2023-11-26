
subjects = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

def show_items():
    for subject,credits in subjects.items():
        print(f'{subject} tiene {credits} creditos')

def sum_credits():
    total_credits = 0

    for credit in subjects.values():
        total_credits += credit

    return total_credits

def main():
    show_items()
    total_credits = sum_credits()

    print(f'\nEl total de creditos es {total_credits}')

if __name__ == "__main__":
    main()