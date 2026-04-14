from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)

        dp = [[0]*(n+1) for _ in range(n+1)]

        pairs.sort(key=lambda x:x[0])

        for i in range(n-1,-1,-1):
            for j in range(i-1,-2,-1):
                exclude = dp[i+1][j+1]

                include = 0
                if j == -1 or pairs[j][1] < pairs[i][0]:
                    include = 1 + dp[i+1][i+1]

                dp[i][j+1] = max(exclude,include)

        return dp[0][0]