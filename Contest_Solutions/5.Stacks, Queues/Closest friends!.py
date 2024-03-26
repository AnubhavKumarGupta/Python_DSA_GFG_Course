#User function Template for python3



def closestFriends(arr,n):
    #Your code here
    
    
    # r = [-1]*n
    # s = []
    # for i in range(n):
    #     while s and arr[i] > arr[s[-1]]:
    #         r[s.pop()] = i
            
    #     s.append(i)
    # return r
    
    
    
    r = []
    s = []
    
    for i in range(n):
        while s and arr[s[-1]] >= arr[i]:
            s.pop()
        if not s:
            r.append(-1)
        else:
            r.append(s[-1])
        s.append(i)
        
    return r
    
    
    