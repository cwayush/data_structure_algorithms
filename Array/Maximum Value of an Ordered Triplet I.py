from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    max_val = max(max_val,(nums[i] - nums[j])*nums[k])

        return max_val

# Approach-1 (Nested Loop)
# T.C : O(n**3)
# S.C : O(1) 

##############################################################################################################################################

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0 
        for k in range(2,n):
            maxPrefix = nums[0]
            for j in range(1,k):
                res = max(res,(maxPrefix - nums[j])*nums[k])
                maxPrefix = max(maxPrefix,nums[j])

        return res

# Approach-2 (Nested Loop)
# T.C : O(n**2)
# S.C : O(1) 

##############################################################################################################################################

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        leftMax = [0]*n
        rightMax = [0]*n

        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1],nums[i-1])
            rightMax[n-1-i] = max(nums[n-i],rightMax[n-i])

        res = 0
        for j in range(1,n-1):
            res = max(res,(leftMax[j] - nums[j])*rightMax[j])

        return res


# Approach-3 (Greedy)
# T.C : O(n)
# S.C : O(n)  

##############################################################################################################################################

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res,dmax * nums[k])
            dmax = max(dmax,imax - nums[k])
            imax = max(imax,nums[k])

        return res
    
# Approach-4 (Greedy Optimise)
# T.C : O(n)
# S.C : O(1) 

sol=Solution()

nums=[12,3,1,2,7]
print(sol.maximumTripletValue(nums))