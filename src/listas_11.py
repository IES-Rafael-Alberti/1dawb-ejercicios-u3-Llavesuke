
def scalar_product(u_vector:list[int],v_vector:list[int]) -> tuple:
    """Make scalar product between 2 vectors

    Args:
        u_vector (list[int]): A vector (list) with three integers value.
        v_vector (list[int]): A vector (list) with three integers value.

    Returns:
        result (list[int]): A new list with the scalar product between the two vectors.
    """
    
    result = tuple(u_vector[i]*v_vector[i] for i in range(len(u_vector)))

    return result

def main():

    u_vector = [120,40,56]
    v_vector = [48,79,25]

    print(scalar_product(u_vector,v_vector))

if __name__ == "__main__":
    main()