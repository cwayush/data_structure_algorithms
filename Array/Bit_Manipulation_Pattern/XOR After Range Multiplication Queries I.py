from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)   
        q = len(queries)

        for l,r,k,v in queries:
            idx = l
            while idx <= min(r,n-1):
                nums[idx] = (nums[idx]*v) % mod
                idx += k

        result = 0
        for n in nums:
            result ^= n

        return result
