from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = count2 = 0
        majEl_1 = majEl_2 = 0

        for num in nums:
            if count1==0 and majEl_2!=num:
                majEl_1 = num
                count1+=1

            elif count2==0 and majEl_1!=num:
                majEl_2 = num
                count2+=1

            elif majEl_1 == num:
                count1+=1

            elif majEl_2 == num:
                count2+=1

            else:
                count1-=1
                count2-=1

        lis = []
        count1 = count2 = 0
        for num in nums:
            if majEl_1 == num:
                count1+=1
            elif majEl_2 == num:
                count2+=1
        compare_length = (len(nums)//3)
        if count1>compare_length:
            lis.append(majEl_1)
        if count2>compare_length:
            lis.append(majEl_2)

        return lis

# Approach-1 (Array_)
# T.C : O(n)
# S.C : O(1) 

sol=Solution()

nums = [3,2,3]
print(sol.majorityElement(nums))