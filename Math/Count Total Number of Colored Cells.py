class Solution(object):
    def coloredCells(self, n):
        total = pow(n,2) + pow(n-1,2)
        return total
    
# Approach-1 (Math)
# T.C : O(1)
# S.C : O(1)   

sol=Solution()

n=4
print(sol.coloredCells(n))