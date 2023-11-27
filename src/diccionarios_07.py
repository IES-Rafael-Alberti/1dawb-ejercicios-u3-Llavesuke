
SHOPPING_CART = {}

def check_values(item,price):
    try:
     if item.isnumeric():
        raise TypeError
     
     if not (price.isnumeric() or price.replace('.','')):
        raise ValueError
     
    except ValueError:
            print('Valor no válido')
            return 'VALOR ERROR'
    except TypeError:
            print('Nombre de artículo no válido')
            return 'TYPE ERROR'
     
def ask_user():
    exit_key = 'exit'
    item = None

    while item != exit_key:

            print('\n--------------------------')
            item = input('¿Que artículo desea? (Escriba exit para salir) -> ')
            
            if item != 'exit':
                price = input('¿Cuanto cuesta? -> ')
                
                check = check_values(item,price)

                if not (check == 'VALOR ERROR' or check == 'TYPE ERROR'):

                    price = float(price)
                    item = item.title()
                    print('--------------------------')

                    SHOPPING_CART.setdefault(item,price)
            else:
                print('\nHasta pronto')
   
def total_cost():
     total = 0
     for price in SHOPPING_CART.values():
          total += price
        
     return total

def main():
     ask_user()
     if not SHOPPING_CART == {}:
        total = total_cost()

        print('\nLista de la compra')

        print('--------------------------')
        for item, price in SHOPPING_CART.items():
            print(f'{item}: {price}')

        print(f'Total: {total}')
        print('--------------------------')

     else:
        print('\n Pero no has comprado nada perro')
    
if __name__ == "__main__":
    main()
    