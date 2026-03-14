from typing import List
from bisect import bisect_left
from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(tasks)
        m = len(workers)
        tasks.sort()
        workers.sort()

        def check(mid):
            p = pills 
            ws = SortedList(workers[m - mid:])

            for i in range(mid-1,-1,-1):
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    rep = ws.bisect_left(tasks[i] - strength)
                    if rep == len(ws):
                        return False
                    p -= 1
                    ws.pop(rep)
            return True

        left = 1
        right = min(m,n)
        ans = 0
        while left<=right:
            mid = (left + right)//2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans

# Approach-1 (SortedList)
# T.C : O(nlogn + mlogm + min(n,m)*log(min(n,m)))
# S.C : O(min(n,m))

sol = Solution()

tasks = [3,2,1]
workers = [0,3,3]
pills = 1
strength = 1
print(sol.maxTaskAssign(tasks,workers,pills,strength))