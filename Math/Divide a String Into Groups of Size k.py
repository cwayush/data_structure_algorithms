from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        not_remaining = (n)%k
        remaining = 0
        if not_remaining!=0:
            remaining = k - not_remaining

        result = []
        s = s + fill*remaining
        i = 0
        while i<len(s):
            result.append(s[i:i+k])
            i+=k
        return result
    
# Approach-1 (Space_Optimal)
# T.C : O(n)
# S.C : O(n)

sol = Solution()

s = "abcdefghi"
k = 3
fill = "x"
print(sol.divideString(s,k,fill))