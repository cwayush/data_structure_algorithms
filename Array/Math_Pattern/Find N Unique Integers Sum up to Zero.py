from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        mid = n//2
        result = []
        for i in range(1,mid + 1):
            result.append(i)
            result.append(-i)

        if n%2 == 1:
            result.append(0)

        return result

# Approach-1 (Traversal)
# T.C : O(n/2)
# S.C : O(n)
    
sol = Solution()

n = 5
print(sol.sumZero(n))