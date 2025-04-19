from bisect import bisect_left,bisect_right
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        count = 0
        nums.sort()
        for i in range(n):
            lower_pair = bisect_left(nums,lower-nums[i],i+1)
            upper_pair = bisect_right(nums,upper-nums[i],i+1)

            count+=(upper_pair - lower_pair)

        return count
    
sol=Solution()

nums = [0,1,7,4,4,5]
lower = 3
upper = 6
print(sol.countFairPairs(nums,lower,upper))