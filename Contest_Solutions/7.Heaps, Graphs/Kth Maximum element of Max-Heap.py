#User function Template for python3

def heapify(arr,n,i):
    lar = i
    l = 2*i + 1
    r = 2*i + 2
     
    if l<n and arr[l]> arr[lar]:
        lar = l
         
    if r<n and arr[r]> arr[lar]:
        lar = r

    if lar != i:
        arr[i], arr[lar] = arr[lar], arr[i]
        heapify(arr,n,lar)
     


def kthMaximumElement(arr,n,k):
    #Your code here
    buildmax(arr,n)
    for _ in range(k-1):
        arr[0]= arr.pop()
        heapify(arr,len(arr),0)
    return arr[0]
        
    #     max_h = arr[:k]
    #     for i in range(k,n):
    #         if arr[i] > max_h[0]:
    #             max_h[0] = arr[i]
    #             heapify(max_h,k,0)
    # return max_h[0]
    
    
def buildmax(arr,n):
    for i in range(n//2 - 1,-1,-1):
        heapify(arr,n,i)
    
    