from collections import Counter
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n=len(nums)
        res=prefix=0
        cnt=Counter([0])
        for i in range(n):
            prefix += 1 if nums[i]%modulo==k else 0
            res += cnt[(prefix-k+modulo)%modulo]
            cnt[prefix%modulo]+=1
        return res
    
# Approach-1 (Hashmap)
# T.C : O(nlogn)
# S.C : O(logn)    

sol=Solution()

nums = [3,2,4]
modulo = 2
k = 1
print(sol.countInterestingSubarrays(nums,modulo,k))