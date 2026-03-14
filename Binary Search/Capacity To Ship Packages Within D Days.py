from typing import List

class Solution:
    def solve_days(self,weights,cap):
        days = 1
        load = 0
        for i in range(len(weights)):
            if load + weights[i]>cap:
                days +=1
                load = weights[i]
            else:
                load +=weights[i]

        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        left = max(weights)
        right = sum(weights)
        while left<=right:
            mid = (left + right)//2
            if self.solve_days(weights,mid)<=days:
                right=mid-1
            else:
                left= mid+1

        return left
    
# Approach-1 (Binary Search)
# T.C : O(n∗log(max(weights)))
# S.C : O(1)

sol=Solution()

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(sol.shipWithinDays(weights,days))