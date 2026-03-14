from typing import List

class Solution:
    def solve(self,i,j1,j2,n,m,grid, dp):
        if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
            return float('-inf')

        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]

        if i == n-1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]

        maxi = float('-inf')
        for c1 in [-1,0,1]:
            for c2 in [-1,0,1]:
                val = 0
                if j1 == j2:
                    val = grid[i][j1]
                else:
                    val = grid[i][j1] + grid[i][j2]
                val += self.solve(i+1,j1+c1,j2+c2,n,m,grid,dp)

                maxi = max(maxi,val)
        dp[i][j1][j2] = maxi

        return dp[i][j1][j2]

    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[[-1]*m for _ in range(m)] for _ in range(n)]

        return self.solve(0,0,m-1,n,m,grid,dp)