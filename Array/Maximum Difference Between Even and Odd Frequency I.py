from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        maxOdd = max(x for x in c.values() if x%2!=0)
        minEven = min(x for x in c.values() if x%2==0)

        return maxOdd - minEven

# Approach-1 (Space_Optimal)
# T.C : O(n)
# S.C : O(1)

sol = Solution()

s = "aaaaabbc"
print(sol.maxDifference(s))