coins = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

def ask_user():
    coin_user = input('Introduce tu moneda -> ')
    
    return coin_user.title()

def main():
    try:
        coin_user = ask_user()
        print(coins[coin_user])
    
    except KeyError:
        print('Moneda no reconocida por el sistema')

if __name__ == "__main__":
    main()