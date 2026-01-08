from typing import List
from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = Counter(nums)

        return max(count,key=count.get)


# Approach-1 (HashMap)
# T.C : O(n)
# S.C : O(k)

sol = Solution()

nums = [1,2,3,3]
print(sol.repeatedNTimes(nums))