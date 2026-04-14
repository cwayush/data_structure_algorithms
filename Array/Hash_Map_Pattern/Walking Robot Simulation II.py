from typing import List

class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir_idx = 0
        self.co_ord = [(1,0),(0,1),(-1,0),(0,-1)]
        self.perimeter = 2 * (width + height) - 4
        self.direction = ['East','North','West','South']

    def step(self, num: int) -> None:

        num %= self.perimeter

        if num == 0 and self.x==0 and self.y==0:
            self.dir_idx = 3

        while num:
            dx,dy = self.co_ord[self.dir_idx]
            nx = self.x + dx
            ny = self.y + dy

            if not (0<=nx<self.w and 0<=ny<self.h):
                self.dir_idx = (self.dir_idx + 1)%4
            
            else:
                self.x = nx
                self.y = ny
                num -= 1

    def getPos(self) -> List[int]:
        return [self.x,self.y]

    def getDir(self) -> str:
        return self.direction[self.dir_idx]
        