#{ 
 # Driver Code Starts
#Initial Template for Python 3




# } Driver Code Ends
#Back-end complete function Template for Python 3

def canReach(mat,n,i,j):
    if i==n-1 and j==n-1:
        return True
    x=False
    y=False
    if j<n-1 and mat[i][j+1]%2==0:
        x=canReach(mat,n,i,j+1)
    if i<n-1 and mat[i+1][j]%2==0:
        y=canReach(mat,n,i+1,j)
    if x==True or y==True:
        return True
    return False

#{ 
 # Driver Code Starts.



if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        mat=[]
        temp=[int(x) for x in input().strip().split()]
        for i in range(0,n*n,n):
            mat.append(temp[i:i+n])
            
       
        if canReach(mat,n,0,0):
            print(1)
        else:
            print(0)
# } Driver Code Ends