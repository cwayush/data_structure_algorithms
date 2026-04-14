from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        
        robot.sort()
        factory.sort()

        factories = []

        for pos,limit in factory:
            factories.extend([pos]*limit)

        n = len(robot)
        m = len(factories)

        dp = [[-1]*(m) for _ in range(n)]

        def solve(i,j):
            if i == n:
                return 0

            if j == m:
                return float('inf')

            if dp[i][j] != -1:
                return dp[i][j]

            skip = solve(i,j+1)

            take = abs(robot[i] - factories[j]) + solve(i+1,j+1)

            dp[i][j] = min(skip,take)
            return dp[i][j]

        return solve(0,0)

