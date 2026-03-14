from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1]*n

        nums.sort()
        arr_idx = [i for i in range(n)]
        last_idx = 0
        maxi = 0

        for idx in range(n):
            for prev in range(idx):
                if nums[idx]%nums[prev] == 0 and 1+dp[prev] > dp[idx]:
                    dp[idx] = 1 + dp[prev]
                    arr_idx[idx] = prev

            if dp[idx]>maxi:
                maxi = dp[idx]
                last_idx = idx

        result=[]
        result.append(nums[last_idx])
        while last_idx!=arr_idx[last_idx]:
            last_idx = arr_idx[last_idx]
            result.append(nums[last_idx])

        return list(reversed(result))

# Approach-1 (Optimise Bottom Up)
# T.C : O(n**2)
# S.C : O(1)   

sol=Solution()

nums = [1,2,4,8]
print(sol.largestDivisibleSubset(nums))