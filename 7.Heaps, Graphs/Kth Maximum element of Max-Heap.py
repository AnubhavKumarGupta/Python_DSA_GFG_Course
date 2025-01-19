#{ 
 # Driver Code Starts
#Initial Template for Python 3

from heapq import heappop, heappush, heapify


# } Driver Code Ends
#Back-end complete function Template for Python 3

def kthMaximumElement(arr,n,k):
    heap=[]
    heapify(heap)
    
    for i in arr:
        heappush(heap,-1*i)
        
    while(k>1):
        k-=1
        heappop(heap)
        
    
    return -1*heap[0]
        
    

#{ 
 # Driver Code Starts.


if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n,k=map(int,input().split())
        arr=[int(x) for x in input().strip().split()]
        
        print(kthMaximumElement(arr,n,k))
        
        
# } Driver Code Ends