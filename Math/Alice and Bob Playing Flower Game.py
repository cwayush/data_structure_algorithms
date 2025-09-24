class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (m*n)//2
    
# Approach-1 (Math)
# T.C : O(1)    
# S.C : O(1)

sol=Solution()
n=3
m=3
print(sol.flowerGame(n,m))