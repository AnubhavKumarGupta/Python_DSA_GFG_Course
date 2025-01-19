def maxValue(s):
    #Your code here
    a = int(s[0])
    for i in range(1,len(s),1):
        b = int (s[i])
        a = max(a+b, a*b)
    return a
        