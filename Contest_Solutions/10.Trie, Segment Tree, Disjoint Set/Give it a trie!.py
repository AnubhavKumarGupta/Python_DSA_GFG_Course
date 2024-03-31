#User function Template for python3

def LCP(ls,n):
    #code here
    if not ls:
        return ""
        
    ml = min(len(s) for s in ls)
    
    prefix = ""
    
    for i in range(ml):
        ch = ls[0][i]
        if all(s[i] == ch for s in ls):
            prefix +=ch
        else:
            break
        
    return prefix
    
    
    