def booleanMatrix(mat, m, n):
    row_marker = [0] * m
    col_marker = [0] * n

    # Mark the rows and columns that need to be updated
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                row_marker[i] = 1
                col_marker[j] = 1

    # Update the matrix based on the markers
    for i in range(m):
        for j in range(n):
            if row_marker[i] == 1 or col_marker[j] == 1:
                mat[i][j] = 1
