
def reverse_list(original_list:list) -> list:
    """Reverse a list
    
    Args:
        original_list (list): A list with any type of data.

    Returns:
        original_list (list): The previous list but reversed.
    """

    original_list.reverse()
    
    return original_list

def main():

    number_list = [1,2,3,4,5,6,7,8,9,10]

    reversed_list = reverse_list(number_list)

    print(reversed_list)

if __name__ == "__main__":
    main()