from typing import List

class Solution:
    def solve(self,r1,c1,r2,grid,n,dp):
        c2 = r1 + c1 - r2

        if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
            return float('-inf')
        
        if grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return float('-inf')

        if r1 == n-1 and c1 == n-1:
            return grid[r1][c1]

        if dp[r1][c1][r2] != -1:
            return dp[r1][c1][r2]
        
        cherry = 0

        if r1 == r2 and c1 == c2:
            cherry = grid[r1][c1]
        
        else:
            cherry = grid[r1][c1] + grid[r2][c2]

        ans = max(
            self.solve(r1+1,c1,r2+1,grid,n,dp),
            self.solve(r1,c1+1,r2,grid,n,dp),
            self.solve(r1+1,c1,r2,grid,n,dp),
            self.solve(r1,c1+1,r2+1,grid,n,dp)
        )

        dp[r1][c1][r2] = cherry + ans

        return dp[r1][c1][r2]

    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dp = [[[-1]*n for _ in range(n)] for _ in range(n)]

        result = self.solve(0,0,0,grid,n,dp)

        return max(0,result)


    