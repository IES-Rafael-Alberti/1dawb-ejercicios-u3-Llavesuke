

def par(numbers):

    pares = [number for number in numbers if number%2 == 0]
    return set(pares)

def three_multiples(numbers):
    multiples = [number for number in numbers if number%3 == 0]
    return set(multiples)

def intersection(pares,multiples):
    return pares&multiples

if __name__ == "__main__":
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    pares = par(numbers)
    print(pares)
    multiples = three_multiples(numbers)
    print(multiples)
    print(intersection(pares,multiples))