from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] == nums[j] and (i*j)%k==0:
                    count+=1
        return count 
    
# Approach-1 (Array)
# T.C : O(n**2)
# S.C : O(1)

sol=Solution()

nums = [3,1,2,2,2,1,3]
k = 2
print(sol.countPairs(nums,k))