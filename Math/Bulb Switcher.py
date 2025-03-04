import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
    
# Approach-1 (Square Root)
# T.C : O(log n)
# S.C : O(1)    

sol=Solution()

n=9
print(sol.bulbSwitch(n))