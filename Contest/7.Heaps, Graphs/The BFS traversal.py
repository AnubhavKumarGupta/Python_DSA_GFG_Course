#Back-end complete function Template for Python 3

def bfs(graph,origin):
    visited = {}
    que = queue.Queue()
    for v in graph:
        visited[v] = False
    que.put(origin)
    visited[origin] = True
    while(que.empty() == False):
        s = que.get();
        print(s,end = " ")
        for i in graph[s]:
            if(visited[i] == False):
                que.put(i)
                visited[i] = True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import queue

if __name__ == '__main__':
    t = int(input())
    while(t>0):
        graph = {}
        E = int(input())
        lst = [int(x) for x in input().strip().split()]
        s = int(input())
        k = 0

        for i in lst:
            if i in graph:
                pass
            else:
                graph[i] = []

        for i in range(E):
            graph[lst[k]].append(lst[k+1])
            k += 2
        bfs(graph,s)
        print()
        t -= 1

# } Driver Code Ends