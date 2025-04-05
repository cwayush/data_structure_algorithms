from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []

        for num in arr:
            if not stack or stack[-1]<=num:
                stack.append(num)
            else:
                maxEl = stack[-1]
                while stack and stack[-1]>num:
                    stack.pop()
                
                stack.append(maxEl)

        return len(stack)
    
# Approach-1 (Monotonic Stack)
# T.C : O(n)
# S.C : O(n)
sol=Solution()

arr = [2,1,3,4,4]
print(sol.maxChunksToSorted(arr))