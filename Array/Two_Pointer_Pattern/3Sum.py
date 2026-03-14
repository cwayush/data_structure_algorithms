from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = len(nums) - 1

            while j<k:
                total = nums[i] + nums[j] + nums[k]

                if total>0:
                    k-=1
                elif total<0:
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1

                    while j<k and nums[j] == nums[j-1]:
                        j+=1

        return res
    
# Approach-1 (Two Pointer)
# T.C : O(nlogn + n^2) => O(n^2)
# S.C : O(n)
        
sol = Solution()

nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))