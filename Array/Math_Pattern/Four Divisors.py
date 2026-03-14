from typing import List 
from math import sqrt

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0

        for num in nums:
            count = 0
            diviSum = 0
            for i in range(1,int(sqrt(num))+1):
                if num%i == 0:
                    d1 = i
                    d2 = num//i

                    if d1==d2:
                        count+=1
                        diviSum+=d1
                    
                    else:
                        count+=2
                        diviSum+=d1+d2
 
            if count == 4:
                total_sum+=diviSum

        return total_sum
    
# Approach-1 (Square Root)
# T.C : O(n * √k)
# S.C : O(1)

sol = Solution()

nums = [21,4,7]
print(sol.sumFourDivisors(nums))