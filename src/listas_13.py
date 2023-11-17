
def ask_user():
    """Ask the user for a serie of integers followed by comma.

    """
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

        except ValueError:
            print('Todos los valores deben ser númericos')

def calculate_average(numeric_list):
    result = 0
    values = len(numeric_list)
    for number in numeric_list:
        result += number

    average = result / values

    return average

def calculate_typical_deviation(numeric_list:list) -> int:
    """Calculate the typical deviation of a list with integers

    Args:
        numeric_list (list[int]): A list with integers introduced by the user.
    Returns:
        typical_deviation (int): The typical deviation from the previous integers.
    """
    values = len(numeric_list)
    
    class_average = sum(numeric_list) / values

    arithmetic_sum = 0

    for number in numeric_list:
        arithmetic_sum += (number - class_average) ** 2
        
    typical_deviation = (arithmetic_sum / values) ** 0.5

    return typical_deviation
    
def main():
    numeric_list = ask_user()

    average = round(calculate_average(numeric_list),2)

    typical_deviation = round(calculate_typical_deviation(numeric_list),2)

    print('Desviación típica: ', end= '')
    print(typical_deviation)

    print('Media: ', end='')
    print(average)

if __name__ == "__main__":
    main()