class Solution:
    def isNegativeWeightCycle(self, n, edges):
        #Code here

        if n == 1:
            return 0
            
        dis = [float('inf') for _ in range(n)]
        dis[edges[0][0]] = 0
        
        for i in range(n-1):
            for i in edges:
                if dis[i[1]] > dis[i[0]] + i[2]:
                    dis[i[1]] = dis[i[0]] + i[2]
                    
        for i in edges:
            if dis[i[1]] > dis[i[0]] + i[2]:
                return 1
        return 0
        
        