import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap=nums
        heapq.heapify(min_heap)

        count_opr = 0
        while len(min_heap)>1 and min_heap[0]<k:
            fs_value = heapq.heappop(min_heap)
            ss_value = heapq.heappop(min_heap)
            n_num = min(fs_value,ss_value)*2 + max(fs_value,ss_value)
            count_opr +=1
            heapq.heappush(min_heap,n_num)

        return count_opr
    
# Approach-1 (min-heap)
# T.C : O(nlogn)
# S.C : O(n) 

sol=Solution()

nums = [1,1,2,4,9] 
k = 20
print(sol.minOperations(nums,k))