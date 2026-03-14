import bisect
class Solution:
    
    def lis(self, arr):
        n=len(arr)
        temp=[]
        temp.append(arr[0])
        lenn=1
        for i in range(1,n):
            if arr[i]>temp[-1]:
                temp.append(arr[i])
                lenn+=1
            else:
                idx = bisect.bisect_left(temp,arr[i])
                temp[idx] = arr[i]
        
        return lenn          
        
sol=Solution()

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(sol.lis(arr))