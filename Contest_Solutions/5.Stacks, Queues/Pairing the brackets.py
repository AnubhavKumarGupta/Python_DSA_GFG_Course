#User function Template for python3

def pairingBrackets(s):
    #Your code here
    p = []
    o = []
    
    for i,c in enumerate(s):
        if c == '(':
            o.append(i)
        elif c == ')':
            if o:
                oi = o.pop(0)
                p.append((oi,i))
    return p
    
    
    
    