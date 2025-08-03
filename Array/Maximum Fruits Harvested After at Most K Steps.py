import bisect
from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        prefix_sum = [0]*n
        position = [0]*n

        for i in range(n):
            position[i] = fruits[i][0]
            prefix_sum[i] = fruits[i][1] + (prefix_sum[i-1] if i>0 else 0)

        maxFruits = 0
        for d in range(0,k//2 +1):
            remain = k - 2*d
            # case 1 (left side go first)
            i = startPos - d
            j = startPos + remain

            left = bisect.bisect_left(position, i)
            right = bisect.bisect_right(position, j)-1
            if left <= right:
                total = prefix_sum[right] - (prefix_sum[left-1] if left > 0 else 0)
                maxFruits = max(maxFruits, total)

            # case 2 (right side go first)
            i = startPos - remain
            j = startPos + d

            left = bisect.bisect_left(position, i)
            right = bisect.bisect_right(position, j)-1
            if left <= right:
                total = prefix_sum[right] - (prefix_sum[left-1] if left > 0 else 0)
                maxFruits = max(maxFruits, total)

        return maxFruits

# Approach-1 (Prefix_sum)
# T.C : O(k*log(n))
# S.C : O(n) 

sol = Solution()

fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
startPos = 5
k = 4

print(sol.maxTotalFruits(fruits,startPos,k))