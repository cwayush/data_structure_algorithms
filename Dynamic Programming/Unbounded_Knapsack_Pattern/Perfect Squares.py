from Math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        maxRange = int(sqrt(n)) + 1

        dp = [[float('inf')] * (n+1) for _ in range(maxRange)]

        for i in range(maxRange):
            dp[i][0] = 0

        for j in range(n+1):
            dp[1][j] = j

        for i in range(2,maxRange):
            for j in range(n+1):
                exclude = dp[i-1][j]
                include = float('inf')
                if (i*i) <= j:
                    include = 1 + dp[i][j-(i*i)]

                dp[i][j] = min(exclude,include)

        return dp[maxRange-1][n]
