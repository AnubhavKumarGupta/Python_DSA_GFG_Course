def pairExists(arr, n, c):
    # Set to store elements encountered
    s = set()
    
    flag = False
    
    for i in range(n):
        # Check if the complement of current element exists in the set
        if c ^ arr[i] in s:
            flag = True
            break
        
        # Insert current element into the set
        s.add(arr[i])
    
    # Output
    if flag:
        return "Yes"
    else:
        return "No"
