#User function Template for python3


def findRoot(i,par,rank1):
    #Your code here
    if par[i] != i:
        par[i] = findRoot(par[i], par, rank1)
    return par[i]
    

def union_(a,b,par,rank1):
    #Your code here
    ra = findRoot(a,par,rank1)
    rb = findRoot(b,par,rank1)
    
    if ra != rb:
        if rank1[ra] < rank1[rb]:
            par[ra] = rb
        elif rank1[ra] > rank1[rb]:
            par[rb] = ra
        else:
            par[rb] = ra
            rank1[ra] += 1



def isConnected(a,b,par,rank1):
    #Your code here
    return findRoot(a,par,rank1) == findRoot(b,par,rank1)
    