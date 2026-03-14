from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        cuts.insert(0, 0)
        cuts.append(n)
        cuts.sort()

        m = len(cuts)

        dp = [[0]*m for _ in range(m)]

        for i in range(m-2, 0, -1):
            for j in range(1, m-1):

                if i > j:
                    continue

                miniCost = float('inf')

                for idx in range(i, j+1):

                    cost = (
                        cuts[j+1] - cuts[i-1]
                        + dp[i][idx-1]
                        + dp[idx+1][j]
                    )

                    miniCost = min(miniCost, cost)

                dp[i][j] = miniCost

        return dp[1][m-2]
