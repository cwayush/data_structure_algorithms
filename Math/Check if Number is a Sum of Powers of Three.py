class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>0:
            if n%3==2:
                return False
            n=n//3
        return True

# Approach-1 (Math)
# T.C : O(log n)
# S.C : O(1)    

sol=Solution()

n=91
print(sol.checkPowersOfThree(n))