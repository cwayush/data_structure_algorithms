from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        n = len(grid)
        m = len(grid[0])
        
        cumm = [[0]*m for _ in range(n)]

        count = 0
        for i in range(n):
            for j in range(m):

                cumm[i][j] = grid[i][j]

                if i > 0:
                    cumm[i][j] += cumm[i-1][j]
                
                if j > 0:
                    cumm[i][j] += cumm[i][j-1]
                
                if i > 0 and j > 0:
                    cumm[i][j] -= cumm[i-1][j-1]

                if cumm[i][j] <= k:
                    count += 1

        return count