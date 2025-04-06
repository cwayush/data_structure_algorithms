class Solution:    
    def minimumPlatform(self,arr,dep):
        n=len(arr)
        arr.sort()
        dep.sort()
        i=j=0
        max_req = count = 0
        while i<n and j<n:
            if arr[i]<=dep[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            max_req=max(max_req,count)
            
        return max_req

# Approach-1 (Two Pointer)
# T.C : O(n*log(n))
# S.C : O(n)
  
sol=Solution()

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(sol.minimumPlatform(arr,dep))