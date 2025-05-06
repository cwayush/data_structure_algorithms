from typing import List

class Solution:
    def check(self,A : List[int], B : int,max_pages : int) -> bool:
        student = 1
        current_pages = 0
        for pages in A:
            if pages>max_pages:
                return False
            if current_pages + pages >max_pages:
                student+=1
                current_pages = pages
                if student>B:
                    return False
                
            else:
                current_pages+=pages
        return True
    
    def allocate_books(self,A : List[int], B : int) -> int:
        low = max(A)
        high = sum(A)
        result = high
        while low<=high:
            mid = (low + high)//2
            if self.check(A,B,mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result

# Approach-1 (Binary_Search)
# T.C : O(n*log(s))         s --> sum of A
# S.C : O(1) 

sol = Solution()

A = [5, 17, 100, 11]
B = 4
print(sol.allocate_books(A,B))


        