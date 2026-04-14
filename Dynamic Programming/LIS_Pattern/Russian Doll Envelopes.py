from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect.bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        return lis([envelope[1] for envelope in envelopes])