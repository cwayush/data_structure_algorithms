from collections import defaultdict,deque
from typing import List

class Solution:

    def topologicalSortCheck(self,adj,indegree,n):
        que = deque()

        count = 0
        for i in range(n):
            if indegree[i]==0:
                count+=1
                que.append(i)

        while que:
            node = que.popleft()

            for n_node in adj[node]:
                indegree[n_node]-=1
                if indegree[n_node]==0:
                    count+=1
                    que.append(n_node)

        if count == n:
            return True

        return False


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        indegree=[0]*numCourses

        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1

        return self.topologicalSortCheck(adj,indegree,numCourses)
    
# Approach-1 (Graph + Topological Sort)
# T.C : O(V+E)
# S.C : O(V+E)

sol = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(sol.canFinish(numCourses,prerequisites))