class Solution:
    def find_flower_indices(self,n,t,arr):
        i = 0
        j = n - 1
        while i < j:
            if arr[i] + arr[j] == t:
                return [i, j]
            elif arr[i] + arr[j] > t:
                j -= 1
            else:
                i += 1
        return [-1, -1]
    
sol=Solution()

n=7
t=5
arr=[1,2,2,4,5,7,10]
print(sol.find_flower_indices(n,t,arr))