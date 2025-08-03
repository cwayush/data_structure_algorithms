from typing import List
from collections import deque

class Solution:
    def bfs(self,node,edges,dist):
        que = deque()

        dist[node] = 0
        visit=[False]*len(edges)
        que.append(node)
        visit[node] = True

        while que:
            u = que.popleft()

            v = edges[u]
            if v != -1 and not visit[v]:
                visit[v] = True
                dist[v] = 1 + dist[u]
                que.append(v)

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        
        distance_1 = [float('inf')]*n
        distance_2 = [float('inf')]*n

        self.bfs(node1,edges,distance_1)
        self.bfs(node2,edges,distance_2)

        minDisNode = -1
        minDistTillnode  = float('inf')

        for i in range(n):
            maxD = max(distance_1[i],distance_2[i])

            if minDistTillnode > maxD:
                minDistTillnode = maxD
                minDisNode = i

        return minDisNode

# Approach-1 (_)
# T.C : O(n)
# S.C : O(n) 

sol = Solution()
edges = [2,2,3,-1]
node1 = 0
node2 = 1
print(sol.closestMeetingNode(edges,node1,node2))