#User function Template for python3


def kSum(a,n,k):
    #Your code here
    result = []
    a.sort()
    total_sum = 0
    for i in range(k):
        total_sum +=a[i]
    # result.append(total_sum)
    return total_sum
    
    
