import heapq
class Solution:
    
    def dijkstra(graph, src):
        dist = {node: float("inf") for node in graph}
        dist[src] = 0
        pq = [(0,src)]
        while pq:
            crdt , crnd = heapq.heappop(pq)
            
            if crdt > dist [crnd]:
                continue
            
            for nei, wei in graph[crnd]:
                dis = crdt + wei
                if dis < dist[nei]:
                    dist[nei] = dis
                    heapq.heappush(pq,(dis,nei))
                    
        return dist



    def solve(V, E, edges, S, K, flagged):
        # code here
        graph = {i: [] for i in range(1,V + 1)}
        
        for u,v,w,in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
            
        dist = solve.dijkstra(graph,S)
        tt= 0
        for node in flagged:
            tt += dist[node]
            
        return tt
        
     
     
# Run Time Error