class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_suff = [-1]*n
        result = []

        min_suff[-1] = s[-1]
        for i in range(n-2,-1,-1):
            min_suff[i] = min(min_suff[i+1],s[i]) 

        stack = []
        for i in range(n):
            stack.append(s[i])

            while stack and (i == n-1 or stack[-1]<=min_suff[i+1]):
                result.append(stack.pop())

        return ''.join(result) 
    
# Approach-1 (Hashmap)
# T.C : O(n)
# S.C : O(n)

sol = Solution()

s = "zza"
print(sol.robotWithString(s))