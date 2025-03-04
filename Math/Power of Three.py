class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n%3==0:
            n=n//3
        return n==1

# Approach-1 (Math)
# T.C : O(log n)
# S.C : O(1)          

sol=Solution()

n=27
print(sol.isPowerOfThree(n))