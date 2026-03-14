from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for t in range(1, target + 1):
            for i in range(1, n + 1):

                dp[i][t] = dp[i-1][t]

                if nums[i-1] <= t:
                    dp[i][t] += dp[n][t - nums[i-1]]

        return dp[n][target]