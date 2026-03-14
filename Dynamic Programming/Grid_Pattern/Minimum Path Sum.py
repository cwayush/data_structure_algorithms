from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[0]*m for _ in range(n)]
        dp[0][0] = grid[0][0]
        
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + grid[i][0]


        for row in range(1,n):
            for col in range(1,m):
                dp[row][col] = grid[row][col] + min(dp[row-1][col], dp[row][col-1])

        return dp[n-1][m-1]