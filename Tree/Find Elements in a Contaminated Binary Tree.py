from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class FindElements:
    def bfs(self,root,x):
        root.val = x
        que =deque([root])
        while que:
            temp = que.popleft()
            self.seen.add(temp.val)
            if temp.left:
                temp.left.val = 2*temp.val + 1
                que.append(temp.left)
            if temp.right:
                temp.right.val = 2*temp.val + 2
                que.append(temp.right)


    def __init__(self, root: Optional[TreeNode]):
        self.seen =set()
        self.bfs(root,0)

    def find(self, target: int) -> bool:
        return target in self.seen 
    
def build_tree(data):
    if not data:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in data]
    for i in range(len(data)):
        if nodes[i] is not None:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                nodes[i].left = nodes[left_idx]
            if right_idx < len(nodes):
                nodes[i].right = nodes[right_idx]
    return nodes[0]

# Input simulation
tree_data = [-1, None, -1]
root = build_tree(tree_data)
obj = FindElements(root)

print(obj.find(1))  
print(obj.find(2))  

# Approach-1 (BFS)
# T.C : O(n)
# S.C : O(n)
