from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        minheap = [(0,0,0)]

        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
         
        visit = [[float('inf')]*m for _ in range(n)]
        visit[0][0]=1

        while minheap:
            currTime,x,y = heapq.heappop(minheap)

            if x==n-1 and y==m-1:
                return currTime
            
            for i in range(4):
                nx = x + dr[i]
                ny = y + dc[i]

                if 0<=nx<n and 0<=ny<m:
                    wait = max(moveTime[nx][ny] - currTime,0)
                    arrTime = currTime + wait + 1

                    if visit[nx][ny] > arrTime:
                        visit[nx][ny] = arrTime
                        heapq.heappush(minheap,(arrTime,nx,ny))

        return -1

# Approach-1 (Dijkstra Algorithm)
# T.C : O(n*m*log(n*m))        
# S.C : O(n*m) 

sol=Solution()

moveTime = [[0,4],[4,4]]
print(sol.minTimeToReach(moveTime))