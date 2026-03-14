from typing import List
from functools import cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        drec = [(-1,1),(1,1),(1,-1),(-1,-1)]
        @cache
        def dfs(row,col,direction,turn,target):
            if not (0<=row<n and 0<=col<m and grid[row][col] == target):
                return 0

            nrow = row + drec[direction][0]
            ncol = col + drec[direction][1]

            max_steps = 1 + dfs(nrow,ncol,direction,turn,2-target)

            if turn == 0:
                nd = (direction + 1) % 4
                nr = row + drec[nd][0]
                nc = col + drec[nd][1]
                max_steps = max(max_steps, 1 + dfs(nr, nc, nd, 1, 2-target))

            return max_steps


        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_res = 0
                    for d in range(4):
                        nrow = i + drec[d][0]
                        ncol = j + drec[d][1]

                        max_res = max(max_res,1+dfs(nrow,ncol,d,0,2))

                    res = max(res,max_res)

        return res
    
# Approach-1 (DFS + Memoization)
# T.C : O(n*m)
# S.C : O(n*m)
    
sol = Solution()
grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
print(sol.lenOfVDiagonal(grid))