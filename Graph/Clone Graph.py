
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldnew = {}

        def dfs(node):
            if node in oldnew:
                return oldnew[node]

            copy = Node(node.val)
            oldnew[node] = copy
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            return copy

        return dfs(node)
    
# Approach-1 (DFS + HashMap)
# T.C : O(V + E)
# S.C : O(V)

sol = Solution()

adjList = [[2,4],[1,3],[2,4],[1,3]]
print(sol.cloneGraph(adjList))
        

        
        
