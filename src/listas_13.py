
def ask_user():
    bool =False
    
    while not bool:
        try:
            sample = input('Introduce una serie de numeros separados por coma \n-> ')

            if not sample.split(','):
                raise TypeError
            
            str_list = sample.split(',')

            for i in range(len(str_list)):
                int(str_list[i])

            for i in range(len(str_list)):
                str_list[i] = int(str_list[i])

            numeric_list = str_list
            
            return numeric_list
        
        except TypeError:
            print('No has puesto bien las comas.')

        except ValueError:
            print('Todos los valores deben ser númericos')

def calculate_average(numeric_list):
    result = 0
    values = len(numeric_list)
    for number in numeric_list:
        result += number

    average = result / values

    return average

def calculate_typical_deviation(numeric_list,average):
    values = len(numeric_list)
    arithmetic_sum = 0

    class_average = (numeric_list[0]+numeric_list[len(numeric_list)])/2

    for number in  numeric_list:
        arithmetic_sum += (number-class_average)

    typical_deviation = ((arithmetic_sum**2)/values)**1/2

    return typical_deviation

def main():
    numeric_list = ask_user()

    average = calculate_average(numeric_list)

    typical_deviation = calculate_typical_deviation(numeric_list,average)

    print('Desviación típica: ', end= '')
    print-(typical_deviation)

    print('Media: ', end='')
    print(average)

if __name__ == "__main__":
    main()