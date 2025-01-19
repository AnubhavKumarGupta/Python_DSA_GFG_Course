#Back-end complete function Template for Python 3

def median(root, k):
    if(root == None):
        return -1
    global v
    v=[]
    inorder(root)
    subtreeRoot = v[k-1]
    v=[]
    inorder(subtreeRoot)
    l = len(v)
    # print(l)
    if(l%2!=0):
        # print("@")
        return v[l//2].data
    else:
        return (v[l//2].data + v[(l//2)-1].data)//2



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        
def insert(root, node):
    if root == None:
        root = node
    else:
        if (root.data <= node.data):
            if root.right == None:
                root.right = node
            else:
                insert(root.right, node)
        elif (root.data > node.data):
            if (root.left == None):
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    global v
    if root:
        inorder(root.left)
        v.append(root)
        inorder(root.right)
        
if __name__ == "__main__":
    t = int(input())
    while(t>0):
        list = [int(x) for x in input().strip().split()]
        n = list[0]
        k = list[1]
        list = [int(x) for x in input().strip().split()]
        root = Node(list[0])
        for i in range(1, n):
            insert(root, Node(list[i]))

        print(median(root, k))
        t=t-1

# } Driver Code Ends