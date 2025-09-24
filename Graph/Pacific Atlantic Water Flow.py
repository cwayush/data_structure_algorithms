from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        for col in range(n):
            p_que.append((0,col))
            p_seen.add((0,col))

        for row in range(1,m):
            p_que.append((row,0))
            p_seen.add((row,0))

        for row in range(m):
            a_que.append((row,n-1))
            a_seen.add((row,n-1))

        for col in range(n-1):
            a_que.append((m-1,col))
            a_seen.add((m-1,col))


        def get_cords(que,seen):
            while que:
                i,j = que.popleft()
                for i_off, j_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r = i + i_off
                    c = j + j_off

                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        que.append((r,c))
                        seen.add((r,c))

        
        get_cords(p_que,p_seen)
        get_cords(a_que,a_seen)

        return list(p_seen.intersection(a_seen))
    
# Approach-1 (BFS)
# T.C : O(m∗n)
# S.C : O(m∗n)

sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(sol.pacificAtlantic(heights))