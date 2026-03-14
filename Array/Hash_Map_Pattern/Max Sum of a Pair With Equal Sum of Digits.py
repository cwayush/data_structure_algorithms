from typing import List

class Solution:
    def getdigit_sum(self,num):
        dig_sum = 0
        while num:
            dig_sum+=num%10
            num=num//10

        return dig_sum

    def maximumSum(self, nums: List[int]) -> int:
        n=len(nums)
        hashtable = [0]*82

        summ=-1
        for i in range(n):
            digitsum = self.getdigit_sum(nums[i])

            if hashtable[digitsum]:
                summ=max(summ,nums[i] + hashtable[digitsum])

            hashtable[digitsum] = max(hashtable[digitsum],nums[i])

        return summ
    
# Approach-1 (Space Optimal)
# T.C : O(n)
# S.C : O(1)

sol=Solution()

input = [18,43,36,13,7]
print(sol.maximumSum(input))
