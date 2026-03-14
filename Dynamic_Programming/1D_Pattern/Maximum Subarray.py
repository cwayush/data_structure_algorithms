from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')

        summ = 0
        for num in nums:
            summ += num
            maxi = max(maxi,summ)

            if summ<0:
                summ = 0

        return maxi