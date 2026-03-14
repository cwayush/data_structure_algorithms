from typing import List

class Solution:

    def dfs(self,i,j,grid,cord,m,n):
        for i_off,j_off in [(0,1),(1,0),(0,-1),(-1,0)]:
            r = i_off + i
            c = j_off + j
            if 0<=r<m and 0<=c<n and grid[r][c] == '1' and (r,c) not in cord:
                cord.add((r,c))
                self.dfs(r,c,grid,cord,m,n)

    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])

        cord = set()
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in cord:
                    cord.add((i,j))
                    self.dfs(i,j,grid,cord,m,n)
                    count +=1

        return count
    
# Approach-1 (DFS)
# T.C : O(n*m)
# S.C : O(n*m)
    
sol = Solution()

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid))