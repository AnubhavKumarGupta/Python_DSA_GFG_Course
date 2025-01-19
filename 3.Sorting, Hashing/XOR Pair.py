def pairExists(arr,n,c):
    s=set()
    for i in range(n):
        if arr[i] not in s:
            s.add(arr[i])
    
    
    for i in range(n):
        if arr[i]^c in s:
            return True
    
    return False
                