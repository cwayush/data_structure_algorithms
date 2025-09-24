from typing import List

class Solution:
    def solve(self,l,r):
        L = 1
        S = 1

        steps = 0
        while (L<=r):
            R = 4*L - 1

            start = max(L,l)
            end = min(R,r)
            if (start<=end):
                steps += (end-start+1)*S

            S +=1
            L = 4*L

        return steps

    def minOperations(self, queries: List[List[int]]) -> int:

        result = 0
        for l,r in queries:
            steps = self.solve(l,r)

            result += (steps+1)//2

        return result
    
# Approach-1 (Traversing)
# T.C : O(n*(log4(r)))
# S.C : O(1)

sol = Solution()

queries = [[1,2],[2,4]]
print(sol.minOperations(queries))