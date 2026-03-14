from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        evenCount=1
        oddCount=0
        result=0
        summ=0
        for num in arr:
            summ+=num
            if summ%2==0:
                result=(result + oddCount)%mod
                evenCount+=1
            else:
                result=(result + evenCount)%mod
                oddCount+=1
        return result
    
sol=Solution()

arr = [1,2,3,4,5,6,7]
print(sol.numOfSubarrays(arr))