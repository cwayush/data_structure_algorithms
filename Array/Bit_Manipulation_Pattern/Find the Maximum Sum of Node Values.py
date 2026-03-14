from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        summ = 0 
        count = 0
        min_diff = float('inf')
        for num in nums:
            if num ^ k > num:
                summ+= num^k
                count+=1

            else:
                summ+= num

            min_diff = min(min_diff,abs(num - (num^k)))

        if count%2==0:
            return summ
        
        return summ - min_diff

sol = Solution()
nums = [1,2,1]
k = 3
edges = [[0,1],[0,2]]
print(sol.maximumValueSum(nums,k,edges))
