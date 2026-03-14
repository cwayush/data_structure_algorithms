from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        seen = [False]*101
        for i in range(n-1,-1,-1):
            if seen[nums[i]]:
                return i//3 +1

            seen[nums[i]] = True

        return 0

# Approach-1 (Array)
# T.C : O(n)
# S.C : O(n)

sol=Solution()

nums = [1,2,3,4,2,3,3,5,7]
print(sol.minimumOperations(nums))