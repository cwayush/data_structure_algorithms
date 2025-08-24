from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i,j = 0,0

        count = 0
        max_subarray = 0

        while i<=j and j<n:
            if nums[j] == 0:
                count+=1
            while count>1:
                if nums[i] == 0:
                    count-=1
                i+=1


            max_subarray = max(max_subarray,j-i)
            j+=1

        return max_subarray

# Approach-1 (Sliding Window)
# T.C : O(n)
# S.C : O(1)  

sol = Solution()

nums = [0,1,1,1,0,1,1,0,1]
print(sol.longestSubarray(nums))