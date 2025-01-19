def rec(node,lvl,req):
    global ans
    if(node == None):
        return
    if(lvl == req):
        ans += 1
    rec(node.left,lvl+1,req)
    rec(node.right,lvl+1,req)


def count(node,l):
    global ans
    ans = 0
    rec(node,1,l)
    return ans