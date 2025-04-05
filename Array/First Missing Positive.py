class Solution(object):
    def firstMissingPositive(self, nums):
        n=len(nums)
        contain_one = False
        for i,num in enumerate(nums):
            if num == 1:
                contain_one = True
            elif num<=0 or num>n:
                nums[i] = 1

        if not contain_one:
            return 1
            
        for num in nums:
            num = abs(num)
            idx = num -1
            if nums[idx]<0:
                continue
            nums[idx] = (-1)*nums[idx]

        for i,num in enumerate(nums):
            if num>0:
                return i+1

        return  n+1

# Approach-1 (Array)
# T.C : O(n)
# S.C : O(1)

sol=Solution()

nums = [7,8,9,11,12]
print(sol.firstMissingPositive(nums))