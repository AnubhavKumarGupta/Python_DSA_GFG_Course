#User function Template for python3

def _push(lst,n):
    # code here
    # minimum  = float('inf')
    # stack = list()
    # for element in lst:
    #     minimum = min(minimum,element)
    #     stack.append([element,minimum])
    #     return stack
    
    
    st = []
    for i in range(n):
        st.append(lst[i])
    return st
    
    
def _getMinAtPop(s,n):
    #code here
    # while s:
    #     getMinimum = s.pop()
    #     print(getMinimum[1],end = " ")
    
    while s != []:
        mini = min(s)
        print(mini,end = " ")
        s.pop()