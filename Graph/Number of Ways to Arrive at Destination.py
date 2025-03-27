from typing import List
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u,v,wt in roads:
            adj[u].append((v,wt))
            adj[v].append((u,wt))

        dist = [float('inf')]*n
        ways = [0]*n
        dist[0] = 0
        ways[0] = 1

        min_heap = [(0,0)]
        mod = 10**9 + 7

        while min_heap:
            path_value,node = heapq.heappop(min_heap)

            for nnode,wt in adj[node]:
                if path_value + wt < dist[nnode]:
                    dist[nnode] = path_value + wt
                    heapq.heappush(min_heap,(dist[nnode],nnode))
                    ways[nnode] = ways[node]

                elif path_value + wt == dist[nnode]:
                    ways[nnode] += ways[node]

        return (ways[n-1]) % mod
    
# Approach-1 (Dijkstra's algorithm)
# T.C : O(n*lon(n))
# S.C : O(n) 
