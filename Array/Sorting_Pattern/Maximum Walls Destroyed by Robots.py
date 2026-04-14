from typing import List
import bisect

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        def count(a, b):
            if a > b:
                return 0
            return bisect.bisect_right(walls, b) - bisect.bisect_left(walls, a)

        coords = sorted(zip(robots, distance))
        n = len(coords)
        walls.sort()

        avail = 0
        cnt = count(coords[0][0] - coords[0][1], coords[0][0] - 1)
        coords.append([float('inf'), 0])
        for i in range(n):
            l, dl = coords[i]
            r, dr = coords[i + 1]

            l1, r1 = l + 1, min(l + dl, r - 1)
            l2, r2 = max(r - dr, l + 1), r - 1
            
            left = count(l1, r1)
            right = count(l2, r2)
            both = left + right - count(max(l1, l2), min(r1, r2))

            navail = max(avail + left, cnt)
            nused = max(avail + both, cnt + right)
            avail, cnt = navail, nused

        for x in set(x for x,_ in coords):
            cnt += count(x, x)
            
        return cnt