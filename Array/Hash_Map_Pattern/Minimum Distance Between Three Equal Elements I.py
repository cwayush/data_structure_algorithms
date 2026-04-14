from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        store = defaultdict(list)

        for i,num in enumerate(nums):
            store[num].append(i)

        
        minDiff = float('inf')
        for el_list in store.values():
            n = len(el_list)
            if n >= 3:
                for i in range(n - 2):
                    diff = 2 * (el_list[i+2] - el_list[i])
                    minDiff = min(minDiff, diff)

        return minDiff if minDiff != float('inf') else -1