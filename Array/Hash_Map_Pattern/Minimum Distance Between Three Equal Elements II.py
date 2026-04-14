from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        store = defaultdict(list)

        for i,num in enumerate(nums):
            store[num].append(i)

        minDiff = float('inf')

        for value in store.values():
            n = len(value)
            if n >= 3:
                for j in range(n-2):
                    res = 2*(value[j+2] - value[j])

                    minDiff = min(minDiff,res)

        return minDiff if minDiff != float('inf') else -1