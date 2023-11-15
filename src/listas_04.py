from listas_03 import clean_terminal

def ask_numbers():
    """Ask the winner numbers to the user

    Returns:
        lottery_numbers (list[int]): A list of integers with the winner numbers of the lottery.

    Raises:
        ValueError: If the number introduced by the user is not a number between 1 and 49.
    """
    lottery_numbers = []

    while len(lottery_numbers) != 6:
        
        try:

            new_number = int(input('Introduce un numero ganador de la lotería \n-> '))
            
            if not new_number in range(1,50):
                raise ValueError
            
            if lottery_numbers.count(new_number):
                    raise TypeError
            
            else:
                lottery_numbers.append(new_number)
    
        except ValueError:
            print('Ha introducido un valor no válido.')
        except TypeError:
            print('No se pueden introducir numeros repetidos')

    return lottery_numbers

def ask_refund():
    """Ask the refund value to the user.

    Returns:
        refund (int): The refund value.
    """
    bool = False
    while not bool:
        try:

            refund = int(input('Introduce el número de reintegro -> '))

            if refund < 0 or refund > 10:
                raise ValueError
            
            return refund
        
        except ValueError:
            print('Numero no valido')
    


def order_list(lottery_numbers:list) -> list:
    """Order the numbers inside of the list from smallest to largest.

    Args:
        lottery_numbers (list[int]): A list with integers with the winners numbers of lottery.

    Returns:
        lottery_numbers (list[int]): A list with integers with the winners numbers of lottery ordered from smallest to largest.
    """

    lottery_numbers.sort()

    return lottery_numbers

def main():

    lottery_numbers = ask_numbers()
    refund_value = ask_refund()

    order_list(lottery_numbers)
    lottery_numbers.append(refund_value)

    clean_terminal()
    
    print('----------------------------------------------------------------')
    print(f'Los numeros ganadores son {lottery_numbers} y el reintegro {refund_value}')
    print('----------------------------------------------------------------')

if __name__ == "__main__":
    main()