from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        actual_area = 0
        seen_corners =set()

        for x1,y1,x2,y2 in rectangles:
            actual_area += (x2-x1)*(y2-y1)

            for corner in [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]:
                if corner in seen_corners:
                    seen_corners.remove(corner)
                
                else:
                    seen_corners.add(corner)

        if len(seen_corners)!=4:
            return False

        minrow = mincol = float('inf')
        maxrow = maxcol = float('-inf')
        for x,y in seen_corners:
            minrow = min(minrow,x)
            maxrow = max(maxrow,x)
            mincol = min(mincol,y)
            maxcol = max(maxcol,y)

        total_area = (maxrow - minrow)*(maxcol-mincol)

        return actual_area == total_area
    
# Approach-1 (Set)
# T.C : O(n)
# S.C : O(n) 
    
sol = Solution()

rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
print(sol.isRectangleCover(rectangles))