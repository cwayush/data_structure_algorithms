from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def solve(nums,idx,curr_xor):
            if idx == len(nums): return curr_xor

            with_num = solve(nums,idx+1,curr_xor ^ nums[idx])

            without_num = solve(nums,idx+1,curr_xor)

            return with_num + without_num

        return solve(nums,0,0)

# Approach-1 (Recursion) 
# T.C : EXPONENTIAL
# S.C : AUXILLARY STACK SPACE

##############################################################################################################################################

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result | num
            
        return result << (len(nums)-1)
    
# Approach-1 (Optimal) 
# T.C : O(n)
# S.C : O(1)
        