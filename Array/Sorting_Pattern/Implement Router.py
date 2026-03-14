from collections import defaultdict, deque
from typing import List
import bisect

class Router:

    def __init__(self, memoryLimit: int):
        self.max_size = memoryLimit
        self.packetStore = {} 
        self.desTimeStore = defaultdict(list)  
        self.que = deque()
        
    def makeKey(self,S,D,T):
        return (S << 40) | (D << 20) | T

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = self.makeKey(source,destination,timestamp)

        if key in self.packetStore:
            return False

        if len(self.packetStore)>=self.max_size:
            self.forwardPacket()
        
        self.packetStore[key] = [source,destination,timestamp]
        self.que.append(key)
        self.desTimeStore[destination].append(timestamp)

        return True

    def forwardPacket(self) -> List[int]:
        if not self.packetStore:
            return []

        key = self.que.popleft()
        packet = self.packetStore.pop(key)
        dest = packet[1]
        self.desTimeStore[dest].pop(0)

        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timeStamps = self.desTimeStore.get(destination,[])
        if not timeStamps:
            return 0

        i = bisect.bisect_left(timeStamps,startTime)
        j = bisect.bisect_right(timeStamps,endTime)

        return j-i
    
# Approach-1 (Queue + HashMap + Binary Search)
# T.C : O(log m)
# S.C : O(m)

sol = Router(3)        

["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]
[[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]

print(sol.addPacket(1,4,90))
print(sol.addPacket(2,5,90))    
print(sol.addPacket(1,4,90))
print(sol.addPacket(3,5,95))
print(sol.addPacket(4,5,105))
print(sol.forwardPacket())
print(sol.addPacket(5,2,110))
print(sol.getCount(5,100,110))
