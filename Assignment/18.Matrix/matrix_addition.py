def subtract_matrices(matrix1, matrix2):
    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for subtraction.")
        return
    
    # Iterate through each element of the matrices and subtract them
    for i in range(len(matrix1)):
        result_row = []
        for j in range(len(matrix1[0])):
            result_row.append(matrix1[i][j] +  matrix2[i][j])
        print(result_row)

# Example matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

# Subtract matrices
print("Result of matrix subtraction:")
subtract_matrices(matrix1, matrix2)
