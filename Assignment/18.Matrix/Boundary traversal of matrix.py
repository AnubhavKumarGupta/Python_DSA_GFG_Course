class Solution:
    def BoundaryTraversal(self, matrix, n, m):
        boundary = []
        r = len(matrix)
        c = len(matrix[0])
        
        if r == 1:
            for i in range(c):
                boundary.append(matrix[0][i])
                
        elif c == 1: 
            for i in range(r):
                boundary.append(matrix[i][0])
                
        else:
            for i in range(c):
                boundary.append(matrix[0][i])
            for i in range(1, r):
                boundary.append(matrix[i][c-1])
            for i in range(c-2, -1, -1):
                boundary.append(matrix[r-1][i])
            for i in range(r-2, 0, -1):
                boundary.append(matrix[i][0])
        
        return boundary
