
numbers_tuple = (50, 75, 46, 22, 80, 65, 8)

def higher_lower(numbers_tuple:tuple) -> int:
    """Get the highest and lowest number from the tuple.

    Args:
        numbers_tuple (tuple[int]): A tuple with integers inside.

    Returns:
        higher (int): The highest number of the tuple.
        lower (int): The lower number of the tuple.
    """
    higher = numbers_tuple[0]
    lower = numbers_tuple[0]
    
    for i in range(len(numbers_tuple)):
        if higher < numbers_tuple[i]:
            higher = numbers_tuple[i]
            
        if lower > numbers_tuple[i]:
            lower = numbers_tuple[i]

    return higher,lower

def main():

    higher,lower = higher_lower(numbers_tuple)
    print(higher)
    print(lower)

if __name__ == "__main__":
    main()