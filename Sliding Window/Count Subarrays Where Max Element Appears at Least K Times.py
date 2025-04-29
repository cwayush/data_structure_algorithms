from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_El = max(nums)
        i=0
        j=0
        result = 0
        count = 0
        n = len(nums)
        while j<n:
            if nums[j]==max_El:
                count+=1

            while count>=k:
                result+= (n-j)

                if nums[i]==max_El:
                    count-=1
                i+=1
            j+=1

        return result
                    
# Approach-1 (Sliding Window)
# T.C : O(n)
# S.C : O()

sol=Solution()

nums = [1,3,2,3,3]
k = 2
print(sol.countSubarrays(nums,k))