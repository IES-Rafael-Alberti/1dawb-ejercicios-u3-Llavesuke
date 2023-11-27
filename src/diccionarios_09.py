import os
import time

BILLS = {}

def clean_terminal():

    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

def menu():
    exit_key = 3
    user_selection = None

    while user_selection != exit_key:
        try:
            user_selection = int(input('1. Añadir factura \n2.Pagar factura \n3.Cerrar sesion\n -> '))
            
            if 1< user_selection > 3:
                raise ValueError
            
            return user_selection

        except ValueError:
            print('**ERROR** selección no válida')
            time.sleep(2)
            clean_terminal()

def ask_bill():
    exit_condition = False
    cost = 'text'

    while not exit_condition:
        try:
            bill_number = input('Introduce el numero de factura -> ')
            "#TODO repeat only cost function"
            cost = int(input('¿Cuanto cuesta la factura? -> '))


            BILLS.setdefault(bill_number,cost)

            exit_condition = True

        except ValueError:
            print('Coste inválido')

def pay_bill() -> int:
    exit_condition = True
    bill_number = 0
    amount = 0
    
    while exit_condition:
        try:
        
            bill_number = input('Número de factura -> ')

            amount = BILLS.pop(bill_number)

            exit_condition += False

        except KeyError:
            print('Número de factura no encontrado.')
        
    return amount

def main():
    exit_condition = True
    total_amount_payed = 0


    while exit_condition:
        unpaid_amount = 0
        bills_numbers = []
        user_selection = menu()
        match user_selection:
            case 1:
                ask_bill()
            case 2:
                payed_amount = pay_bill()

                total_amount_payed += payed_amount
            case 3:
                exit_condition = False
        
        for values in BILLS.values():
            unpaid_amount += values
        
        for keys in BILLS.keys():
            bills_numbers.append(keys)

        show_list = ('-').join(bills_numbers)

        clean_terminal()
        print('----------------')
        print(f'Facturas sin pagar: {show_list}')
        print(f'Cantidad pagada: {total_amount_payed}')
        print(f'Cantidad sin pagar {unpaid_amount}')
        print('----------------')

if __name__ == "__main__":
    main()