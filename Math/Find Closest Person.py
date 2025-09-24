class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_reach = abs(z-x)
        y_reach = abs(z-y)
        if x_reach == y_reach:
            return 0
        elif x_reach<y_reach:
            return 1

        return 2
    
# Approach-1 (Math)
# T.C : O(1)    
# S.C : O(1)

sol = Solution()
x=1
y=2
z=3
print(sol.findClosest(x,y,z))
    