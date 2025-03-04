from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result=[]
        n= len(nums1)
        m= len(nums2)
        i,j=0,0
        while i<n and j<m:
            if nums1[i][0] == nums2[j][0]:
                new_val = nums1[i][1] + nums2[j][1]
                nums1[i][1] = new_val
                result.append(nums1[i])
                i+=1
                j+=1
            
            elif nums1[i][0]<nums2[j][0]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1

        while i<n:
            result.append(nums1[i])
            i+=1

        while j<m:
            result.append(nums2[j])
            j+=1
        return result

# Approach-1 (Two POinter)
# T.C : O(n+m)
# S.C : O(n+m)

sol=Solution()

nums1 = [[2,4],[3,6],[5,5]] 
nums2 = [[1,3],[4,3]]
print(sol.mergeArrays(nums1,nums2))