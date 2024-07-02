#User function Template for python3

from collections import defaultdict, deque

def bfs(graph,origin):
    visit = set()
    queue = deque([origin])
    
    while queue:
        ver = queue.popleft()
        if ver not in visit:
            print(ver, end =" ")
            visit.add(ver)
            
            for av in graph[ver]:
                if av not in visit:
                    queue.append(av)