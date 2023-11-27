
MONTH = {1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'}

def ask_date():
    flag = True
    separated_date = []

    while flag:
        try:
            date = input('Introduce la fecha en el formato dd/mm/aaaa -> ')
            separated_date = date.split('/')

            if not len(separated_date[0]) == 2 or not len(separated_date[1]) == 2 or not len(separated_date[2]) == 4:
                raise TypeError
            
            flag = False

        
        except TypeError:
            print('Formato no válido')

    return separated_date

def select_month(date):
    name_month = MONTH[int(date[1])]

    return name_month

def main():
    separated_date = ask_date()


    name_month = select_month(separated_date)

    print(f'\n{separated_date[0]} de {name_month} de {separated_date[2]}')

if __name__ == "__main__":
    main()