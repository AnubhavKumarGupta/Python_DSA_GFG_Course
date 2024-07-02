#User function Template for python3

#class Node:
#    def __init__(self,key): 
#        self.left = None
#        self.right = None
#        self.val = key

from collections import deque

def count(node,level):
    #your code here
    if not node:
        return 0
        
    queue = deque([(node),0])
    lc = 0
    while queue:
        nd, lvl= queue.popleft()
        if lvl == level:
            lc += 1
                
        if lvl < level:
            if nd.left:
                queue.append((nd.left, lvl + 1 ))
                        
            if nd.right:
                queue.append((nd.right, lvl + 1))
                

    return lc



# Undone