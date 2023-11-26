

def residence_list(bill_data: list) -> set:
    residence_list = set()

    for individual_bill in bill_data:
        residence_list.add(individual_bill[3])

    return residence_list

def main():
    bill_data = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]

    domicilies = residence_list(bill_data)

    for domicilie in domicilies:
        print(domicilie)

if __name__ == "__main__":
    main()
    
        