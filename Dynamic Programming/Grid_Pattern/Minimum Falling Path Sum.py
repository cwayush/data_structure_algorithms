from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = [[0]*n for _ in range(n)]

        for col in range(n):
            dp[0][col] = matrix[0][col]

        for row in range(1,n):
            for col in range(n):
                
                up = dp[row-1][col]
                left = dp[row-1][col-1] if col > 0 else float('inf')
                right = dp[row-1][col+1] if col < n-1 else float('inf')

                dp[row][col] = matrix[row][col] + min(up, left, right)
        
        return min(dp[n-1])

