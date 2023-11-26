data = {}

def ask_name():
    bool = True
    while bool:
        try:

            name = input('¿Cual es su nombre? -> ')
            if name.isnumeric():
                raise TypeError
            data['name'] = name
            
            bool = False

        except TypeError:
            print('Su nombre debe ser solo letras')

def ask_age():
    bool = True
    while bool:
        try:
            age = int(input('¿Cual es su edad? -> '))
            data['age'] = age
            bool = False
        
        except(ValueError):
            print('ERROR')

def ask_adress():
    adress = input('¿Cual es su dirección? -> ')
    
    data['adress'] = adress 

def ask_phone():
    bool = True
    while bool:
        try:
            phone = input('¿Cual es su número de telefono? -> ')
            if not len(phone) == 9:
                raise TypeError
            data['phone'] = phone
            bool = False
         
        except TypeError:
            print('Formato incorrecto')


def main():
    ask_name()
    ask_age()
    ask_adress()
    ask_phone()

    print('-----------------------------------------------------------------------------------------------------')
    print(data.get('name'), 'tiene', data.get('age'), 'años, vive en', data.get('adress'), 'y su número de teléfono es', data.get('phone'))
    print('-----------------------------------------------------------------------------------------------------')

if __name__ == "__main__":
    main()