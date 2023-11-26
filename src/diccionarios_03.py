fruits = {'platano': 1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja':0.70}

def ask_user():
    flag = True
    while flag:
        try:
            user_fruit = input('¿Cual fruta quieres comprar? -> ')
            if user_fruit.isnumeric():
                raise TypeError
            
            fruits[user_fruit.lower()]

            return user_fruit.lower()
        
        except TypeError:
            print('Nombre de fruta inválido')
        except KeyError:
            print('No vendemos esa fruta')

def ask_kilos():
    flag = True
    while flag:
        try:

            kilos = int(input('¿Cuantos kilos quieres? -> '))

            return kilos
        
        except ValueError:
            print('ERROR, formato inválido')

def calcule_price(user_fruit,kilos):
    price = fruits[user_fruit]*kilos

    return price

def main():
    print('-----------------------------')
    fruit = ask_user()
    kilo = ask_kilos()

    price = round(calcule_price(fruit,kilo),2)

    print(f'Cuesta {price}')
    print('-----------------------------')


if __name__ == "__main__":
    main()