from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        summ = 0
        max_Product = 0
        mod = 10**9 + 7

        def total_sum(root):
            nonlocal max_Product,summ
            if root is None:
                return 0

            left = total_sum(root.left)
            right = total_sum(root.right)

            subTreeSum = left + right + root.val

            product = (summ - subTreeSum)*subTreeSum
            max_Product = max(max_Product,product)

            return subTreeSum
            
        summ = total_sum(root)
        total_sum(root)

        return (max_Product) % mod

# Approach-1 (DFS)
# T.C : O(n)
# S.C : O(n)

sol= Solution()

root = [1,2,3,4,5,6]
