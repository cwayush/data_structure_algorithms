from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        candiesCollect = 0
        found_box = set()
        visited = set()

        que = deque()
        for box in initialBoxes:
            found_box.add(box)
            if status[box]==1:
                que.append(box)
                visited.add(box)
                candiesCollect += candies[box]

        while que:
            box = que.popleft()

            for new_box in containedBoxes[box]:
                found_box.add(new_box)
                if status[new_box]==1 and new_box not in visited:
                    que.append(new_box)
                    visited.add(new_box)
                    candiesCollect += candies[new_box]

            for box_key in keys[box]:
                status[box_key] = 1
                if box_key in found_box and box_key not in visited:
                    que.append(box_key)
                    visited.add(box_key)
                    candiesCollect += candies[box_key]

        return candiesCollect
    
sol = Solution()

status = [1,0,1,0]
candies = [7,5,4,100]
keys = [[],[],[1],[]]
containedBoxes = [[1,2],[3],[],[]]
initialBoxes = [0]
print(sol.maxCandies(status,candies,keys,containedBoxes,initialBoxes))