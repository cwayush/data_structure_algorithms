from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])

        dp = [[0]*m for _ in range(n)]

        dp[n-1][m-1] = max(1,1 - dungeon[n-1][m-1])

        for row in range(n-1,-1,-1):
            for col in range(m-1,-1,-1):
                if row == n-1 and col == m-1:
                    continue
                
                right = dp[row][col+1] if col+1<m else float('inf')
                bottom = dp[row+1][col] if row+1<n else float('inf')

                need = min(right,bottom) - dungeon[row][col]

                dp[row][col] = max(1,need)

        return dp[0][0]                
