#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict


# Contributed by: Nagendra Jha

cur_scc_size = 0  # stores size of current scc

# This class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        # A function used by DFS

    def DFSUtil(self, v, visited):
        global cur_scc_size
        # Mark the current node as visited and count it
        visited[v] = True
        cur_scc_size += 1
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

        # Function that returns reverse (or transpose) of this graph

    def getTranspose(self):
        g = Graph(self.V)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

        # The main function that finds and prints all strongly
    

    # connected components
    
# } Driver Code Ends
    #Back-end complete function Template for Python 3
    
    
    def getMaxsize(self):
        global cur_scc_size
        max_size = 1  # initial max size.. 1
        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited = [False] * (self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
    
                # Create a reversed graph
        gr = self.getTranspose()
    
        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * (self.V)
    
        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i] == False:
                cur_scc_size = 0 # initialize curr scc size as 0
                gr.DFSUtil(i, visited)
                max_size = max(max_size, cur_scc_size)
        return max_size  # return the answer


#{ 
 # Driver Code Starts.
    


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = map(int, input().strip().split())
        g = Graph(V)
        for i in range(E):
            u, v = map(int, input().strip().split())
            g.addEdge(u - 1, v - 1)
        print(g.getMaxsize())
# } Driver Code Ends