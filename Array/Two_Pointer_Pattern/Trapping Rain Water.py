class Solution(object):
    def trap(self, height):
        lmax = rmax = 0
        total= 0 
        l = 0
        r = len(height)-1
        while l<r:
            if height[l] < height[r]:
                if lmax > height[l]:
                    total += lmax - height[l]
                else:
                    lmax = height[l]
                l+=1

            else:
                if rmax > height[r]:
                    total += rmax - height[r]
                else:
                    rmax = height[r]
                r-=1
            
        return total

# Approach-1 (Two Pointer)
# T.C : O(n)
# S.C : O(1)

sol=Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))
