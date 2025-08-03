from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        heap = []
        i = 0
        count = 0
        day = events[0][0]

        while i<n or heap:

            if not heap:
                day = events[i][0]

            while i<n and day == events[i][0]:
                heapq.heappush(heap,events[i][1])
                i+=1

            while heap and heap[0]<day:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                count+=1

            day+=1

        return count
    
# Approach-1 (min-heap)
# T.C : O(nlogn)
# S.C : O(n) 
    
sol = Solution()

events= [[1,2],[2,3],[3,4],[1,2]]
print(sol.maxEvents(events))