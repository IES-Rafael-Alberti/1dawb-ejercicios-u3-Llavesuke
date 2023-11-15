
def display_matrix(A):
    print('Matriz: ')
    for row in A:
        print(row)

    print('\n')

def matrix_products(A,B):
    rows_A = len(A)
    columns_A = len(A[0])
    
    columns_B = len(B[0])


    C = [[0 for _ in range(columns_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(columns_B):
            for k in range(columns_A):
                C[i][j] += A[i][k] * B[k][j]

    return C

def main():
    A = [[1,2,3],
         [4,5,6]]
    
    B = [[-1,0],
         [0,1],
         [1,1]]

    display_matrix(A)
    display_matrix(B)

    C = matrix_products(A,B)

    display_matrix(C)

if __name__ == "__main__":
    main()