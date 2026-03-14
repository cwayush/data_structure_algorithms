class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = list(str(n))
        length = len(arr)
        i = length - 2
        while i>=0 and arr[i]>=arr[i+1]:
            i-=1
        if i == -1:
            return -1

        k = length - 1
        while arr[k]<=arr[i]:
            k-=1

        arr[i],arr[k] = arr[k],arr[i]

        arr = arr[:i+1] + arr[i+1:][::-1]

        final_ans = int(''.join(arr))
        
        return final_ans if final_ans<=2**31 - 1 else -1
    
# Approach-1 (Two Pointer)
# T.C : O(n)
# S.C : O(1) 

sol=Solution()

n = 1099011
print(sol.nextGreaterElement(n))


# TESTCASE: 1, 10001, 1099011, 2147483647, 2147483486, 117722222, 111177777, 888887771, 111000222, 99999999, 1020040, 887755443, 9988776655