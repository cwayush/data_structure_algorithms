from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        dir_idx = 0
        x,y = 0,0
        max_dis = 0

        obstacle = set(map(tuple,obstacles))

        for comm in commands:
            if comm == -2:
                dir_idx = (dir_idx + 3)%4
            
            elif comm == -1:
                dir_idx = (dir_idx + 1)%4

            else:
                dx,dy = directions[dir_idx]

                for _ in range(comm):
                    nx = x + dx
                    ny = y + dy

                    if (nx,ny) in obstacle:
                        break

                    x = nx
                    y = ny

                    max_dis = max(max_dis, x*x + y*y)

        return max_dis