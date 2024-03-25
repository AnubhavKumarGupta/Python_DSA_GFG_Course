#User function Template for python3

def avgOfString(s):
    #code here
    t = 0
    l = len(s)
    for c in s:
        t += ord(c)
    return t // l
