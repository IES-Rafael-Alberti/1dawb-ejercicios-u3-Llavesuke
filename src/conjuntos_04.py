

def common(frutas1,frutas2):
    return frutas1 | frutas2

def difference(frutas1,frutas2):
    return frutas1-frutas2

def difference2(frutas1,frutas2):
    return frutas2-frutas1

def main():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    frutas1 = set(frutas1)
    frutas2 = set(frutas2)

    print(common(frutas1,frutas2))
    print(difference(frutas1,frutas2))
    print(difference2(frutas1,frutas2))

if __name__ == "__main__":
    main()