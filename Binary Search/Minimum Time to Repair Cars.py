from typing import List
import math

class Solution:
    def isPossible(self,time,ranks,cars):
        carFixed = 0
        for rank in ranks:
            carFixed+=int(math.sqrt(time//rank))

        return carFixed>=cars

    def repairCars(self, ranks: List[int], cars: int) -> int:
        result =-1
        left = 1
        right = max(ranks)*cars*cars

        while left<=right:
            mid = (left + right)//2
            if self.isPossible(mid,ranks,cars):
                result = mid
                right = mid-1
            else:
                left = mid+1

        return result
    
# Approach-1 (Binary_Search)
# T.C : O(log(Max(Ranks)∗Cars∗Cars))
# S.C : O(1) 



sol=Solution()

ranks = [4,2,3,1]
cars = 10
print(sol.repairCars(ranks,cars))