def conjunto_potencia(original_set):
    original_list = list(original_set)
    n = len(original_list)
    result = [[]]

    i = 0
    while i < n:
        current_element = original_list[i]
        new_subset = [subset + [current_element] for subset in result]
        result.extend(new_subset)
        i += 1

    ordered_result = []
    for subset in result:
        ordered_result.append(subset)

    ordered_result.sort(key=len)

    return [set(subset) for subset in ordered_result]


def main():
    example_set = {0,1, 2}
    result = conjunto_potencia(example_set)

    print(result)

if __name__ == "__main__":
    main()