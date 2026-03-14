from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_seen = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in nums_seen:
                length = 1

                while (num + length) in nums_seen:
                    length+=1
                longest = max(longest,length)

        return longest
    
# Approach-1 (HashSet)
# T.C : O(n)
# S.C : O(n)
                
sol = Solution()

nums = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(nums))