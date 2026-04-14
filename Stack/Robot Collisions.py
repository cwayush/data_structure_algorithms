from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(healths)

        robots = sorted(zip(positions,healths,directions,range(n)))

        stack = []

        for pos,health,direction,idx in robots:
            curr_health = health

            if direction == 'R':
                stack.append([curr_health,direction,idx])
            
            else:
                while stack and stack[-1][1] == 'R':
                    top = stack[-1]

                    if top[0] < curr_health:
                        stack.pop()
                        curr_health -= 1
                    elif top[0] == curr_health:
                        stack.pop()
                        curr_health = 0
                        break
                    else:
                        top[0] -= 1
                        curr_health = 0
                        break

                if curr_health > 0:
                    stack.append([curr_health,direction,idx])

        stack.sort(key=lambda x:x[2])

        return [h for h,d,i in stack]
