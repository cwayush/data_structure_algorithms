from typing import List

class Solution:
    def longestBitonicSequence(self, n : int, nums : List[int]) -> int:
        
        lis = [1] * n
        lds = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], lds[j] + 1)
        
        maxLen = 0
        
        for i in range(n):
            if lis[i] > 1 and lds[i] > 1:  
                maxLen = max(maxLen, lis[i] + lds[i] - 1)
        
        return maxLen
