from typing import List
from collections import deque

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        not_abl = [False]*(days+1)

        for start,end in meetings:
            for i in range(start,end+1):
                not_abl[i] = True

        count_day = 0
        for i in range(1,days+1):
            if not_abl[i] == 0:
                count_day+=1
        
        return count_day

    
# Approach-1 (Brute Force)
# T.C : O(n*days)
# S.C : O(n) 

##############################################################################################################################################

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        que =deque([(meetings[0][0],meetings[0][1])])
        for i in range(1,len(meetings)):
            if que[-1][1]>=meetings[i][0] -1 :
                start,end = que.pop()
                que.append((start,max(end,meetings[i][1])))
            else:
                que.append((meetings[i][0],meetings[i][1]))

        busy_days =0
        for start,end in que:
            busy_days += (end - start + 1)

        return days - busy_days
    
# Approach-1 (Queue Method)
# T.C : O(n*log(n))
# S.C : O(n) 

##############################################################################################################################################

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        end = 0
        days_off = 0
        for i in range(len(meetings)):
            if meetings[i][0]>end:
                days_off +=  meetings[i][0] - end -1

            end = max(end,meetings[i][1])

        if end<days:
            days_off += days - end

        return days_off 
    
# Approach-1 (Queue Method)
# T.C : O(n*log(n))
# S.C : O(1) 




        