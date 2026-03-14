from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]

        def house_rob(nums):
            n = len(nums)

            if n == 0:
                return 0
            if n == 1:
                return nums[0]

            dp = [0]*(n)
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])

            for i in range(2,n):
                dp[i] = max(dp[i-1],dp[i-2] + nums[i])

            return dp[n-1]

        temp1 = []
        temp2 = []

        for i in range(n):
            if i!=0:
                temp1.append(nums[i])
            if i!=n-1:
                temp2.append(nums[i])

        return max(house_rob(temp1),house_rob(temp2))