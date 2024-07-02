#User function Template for python3

def canReach(mat,n,i,j):
    #Your code here
    if i == n - 1 and j == n - 1:
        return mat[i][j] %2 == 0
        
    if i >=n or j >=n or mat[i][j] %2 != 0:
        return False
    
    return canReach(mat, n, i + 1, j) or canReach(mat, n, i, j + 1)


def ispossible(mat,n):
    return 1 if canReach(mat,n) else 0
    
    