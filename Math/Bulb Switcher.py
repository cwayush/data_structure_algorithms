import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
    
sol=Solution()

n=9
print(sol.bulbSwitch(n))