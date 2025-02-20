from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        result=""
        curr_str=[]
        seen=(nums)
        def solve(j):
            nonlocal curr_str,result,seen
            if j==n:
                n_nums = ''.join(curr_str)
                if n_nums not in seen:
                    result = n_nums
                return 

            for val in [0,1]:
                curr_str.append(str(val))
                solve(j+1)
                curr_str.pop()


        solve(0)
        return result
    
# Approach-1 (Backtracking)
# T.C : O(2^n)
# S.C : O(n) 

##############################################################################################################################################

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        result=""
        for i in range(n):
            ch=nums[i][i]
            
            result+='1' if ch=='0' else '0'

        return result
    
# Approach-2 (Array Traverse)
# T.C : O(n)
# S.C : O(1) 

sol=Solution()

nums=['111','011','001']
print(sol.findDifferentBinaryString(nums))