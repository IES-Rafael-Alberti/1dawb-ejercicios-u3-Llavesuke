
data = {}

def ask_user():
    flag = True
    while flag:

            type_input = (input('Que tipo de dato vas a introducir -> ')).title() 
            if type_input == 'Exit':
                 flag = False
            else:
                data_input = input('Dato -> ')

                data.setdefault(type_input, data_input)
                print('-----------------')
                for key,value in data.items():
                    print(f'{key}: {value}')
                print('-----------------')


def main():
    ask_user()

if __name__ == "__main__":
    main()