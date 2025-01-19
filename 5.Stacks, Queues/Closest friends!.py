def closestFriends(arr,n):
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
    